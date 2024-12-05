import pandas as pd
import chardet

"""
regional_charts.csv파일에서 date,country,artists열만 가져와서 저장.
date열 문자열 형식을 yyyy/mm/dd -> yyyy로 변환
"""


path = "./regional_charts.csv"
chunk_size = 100000
chunks = []
category = ["date","country","artists"]
for chunk in pd.read_csv(path,chunksize = chunk_size):
    chunk = chunk[category]
    chunk['year'] = chunk['date'].str[:4]
    chunks.append(chunk)
df = pd.concat(chunks, axis = 0)
df.drop(columns=["date"])
df.to_csv("./year_country_artists.csv")