# 라이브러리 가져오기
import wikipedia
from sentence_transformers import SentenceTransformer
import chromadb

# 1단계: 문서 가져오기 + 청킹 (이전과 동일)
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

print("조각 개수:", len(chunks))

# 2단계: 임베딩 모델 불러오기
print("모델 불러오는 중...")
model = SentenceTransformer("intfloat/multilingual-e5-small")

# 3단계: ChromaDB 준비 (저장 공간 만들기)
client = chromadb.Client()                          # ChromaDB 시작
collection = client.create_collection("semiconductor")  # "semiconductor" 보관함 생성

# 4단계: 조각 + 임베딩을 DB에 저장
print("DB에 저장 중...")
embeddings = model.encode(chunks)
collection.add(
    documents=chunks,                               # 원본 글 조각
    embeddings=embeddings.tolist(),                 # 그 숫자(임베딩)
    ids=[f"chunk_{i}" for i in range(len(chunks))]  # 각 조각의 이름표 (chunk_0, chunk_1...)
)
print("저장 완료! 총", collection.count(), "개")

# 5단계: 질문하고 검색하기 (핵심!)
question = "What is photoresist?"                   # 질문
print("\n질문:", question)

# 질문도 임베딩으로 변환
question_embedding = model.encode([question])

# DB에서 가장 비슷한 조각 3개 찾기
results = collection.query(
    query_embeddings=question_embedding.tolist(),
    n_results=3                                     # 상위 3개
)

# 결과 출력
print("\n=== 가장 관련 있는 조각 3개 ===")
for i, doc in enumerate(results["documents"][0]):
    print(f"\n[{i+1}번째]")
    print(doc)