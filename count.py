import pandas as pd

# 데이터 읽기
df = pd.read_csv("2023_filtered.csv")

# Country와 Artist_country별 등장 빈도 계산
frequency_df = df.groupby(['country', 'artists_country']).size().reset_index(name='count')

# 결과 저장
frequency_df.to_csv("artist_country_distribution.csv", index=False)
