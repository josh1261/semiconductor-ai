# 필요한 라이브러리 가져오기
import wikipedia
from sentence_transformers import SentenceTransformer

# 1단계: 문서 가져오기 + 청킹 (지난번과 동일)
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
print("모델 불러오는 중... (처음엔 다운로드라 1~2분 걸려요)")
model = SentenceTransformer("intfloat/multilingual-e5-small")

# 3단계: 조각들을 숫자로 변환 (임베딩)
print("임베딩 중...")
embeddings = model.encode(chunks)

# 4단계: 결과 확인
print("---")
print("임베딩 개수:", len(embeddings))
print("숫자 1개의 길이(차원):", len(embeddings[0]))
print("첫 조각의 임베딩 앞 10개 숫자:")
print(embeddings[0][:10])