# 라이브러리 가져오기
import wikipedia
from sentence_transformers import SentenceTransformer
import chromadb
import ollama

# 1단계: 문서 가져오기 + 청킹
wikipedia.set_lang("en")
page = wikipedia.page("Photolithography")
text = page.content

chunk_size = 300
overlap = 50
chunks = []
start = 0
while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start = end - overlap

# 2단계: 임베딩 모델 + 벡터 DB
model = SentenceTransformer("intfloat/multilingual-e5-small")
client = chromadb.Client()
collection = client.create_collection("semiconductor")

embeddings = model.encode(chunks)
collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
print("DB 준비 완료! 총", collection.count(), "개 조각")

# 3단계: 질문 → 검색
question = "What is photoresist?"
print("\n질문:", question)

question_embedding = model.encode([question])
results = collection.query(
    query_embeddings=question_embedding.tolist(),
    n_results=3
)
found_chunks = results["documents"][0]   # 찾은 조각 3개

# 4단계: 찾은 조각을 LLM에게 전달 → 답변 생성 (핵심!)
# 찾은 조각들을 하나의 참고자료로 합치기
context = "\n".join(found_chunks)

# LLM에게 줄 지시문 (프롬프트)
prompt = f"""다음 자료를 참고해서 질문에 답해줘.

[참고 자료]
{context}

[질문]
{question}

[답변]"""

# Ollama로 답변 생성
print("\nLLM이 답변 생성 중...")
response = ollama.chat(
    model="gemma2:2b",
    messages=[{"role": "user", "content": prompt}]
)

# 5단계: 결과 출력
print("\n=== LLM 답변 ===")
print(response["message"]["content"])