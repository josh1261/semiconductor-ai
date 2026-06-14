# wikipedia 라이브러리 가져오기
import wikipedia

# 위키피디아 언어를 영어로 설정
wikipedia.set_lang("en")

# "Photolithography" 페이지 가져오기
page = wikipedia.page("Photolithography")

# 페이지 제목 출력
print("제목:", page.title)

# 내용 앞부분 500글자만 출력 (전체는 너무 기니까)
print("내용 일부:")
print(page.content[:500])