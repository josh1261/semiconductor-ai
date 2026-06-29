import sys
import pandas as pd
import pickle

# 옛 모듈 이름을 최신 위치로 "통역"
import pandas.core.indexes
sys.modules["pandas.indexes"] = pandas.core.indexes
import pandas.core.indexes.base
sys.modules["pandas.indexes.base"] = pandas.core.indexes.base

# 데이터 읽기 (latin1 인코딩으로)
print("데이터 불러오는 중... (2GB라 시간 좀 걸려요)")
with open("data/LSWMD.pkl", "rb") as f:
    df = pickle.load(f, encoding="latin1")

print("\n데이터 크기:", df.shape)
print("\n열 이름:", df.columns.tolist())
print("\n=== 앞 5개 데이터 ===")
print(df.head())