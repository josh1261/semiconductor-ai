# pandas 가져오기
import pandas as pd

# .pkl 데이터 불러오기
print("데이터 불러오는 중... (2GB라 시간 좀 걸려요)")
df = pd.read_pickle("data/LSWMD.pkl")

# 1. 데이터 크기 (행, 열)
print("\n데이터 크기:", df.shape)

# 2. 열(컬럼) 이름 보기
print("\n열 이름:", df.columns.tolist())

# 3. 앞부분 5개 살펴보기
print("\n=== 앞 5개 데이터 ===")
print(df.head())