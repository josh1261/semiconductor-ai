# wikipedia 라이브러리 가져오기
import wikipedia

# 위키에서 문서 가져오기 (지난번과 동일)
wikipedia.set_lang("en")
page = wikipedia.page("Photolithography")
text = page.content

# 청킹 설정
chunk_size = 300      # 조각 하나의 글자 수
overlap = 50          # 조각끼리 겹치는 글자 수

# 청킹 실행
chunks = []                          # 조각들을 담을 빈 목록
start = 0                            # 자르기 시작 위치
while start < len(text):             # 글 끝까지 반복
    end = start + chunk_size         # 끝 위치 = 시작 + 300
    chunk = text[start:end]          # 그 구간을 잘라냄
    chunks.append(chunk)             # 목록에 추가
    start = end - overlap            # 다음 시작 = 끝 - 50 (겹치게)

# 결과 확인
print("전체 글자 수:", len(text))
print("조각 개수:", len(chunks))
print("---")
print("첫 번째 조각:")
print(chunks[0])
print("---")
print("두 번째 조각:")
print(chunks[1])