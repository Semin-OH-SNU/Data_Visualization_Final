import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
from ast import literal_eval


path = ".\Data\prepared.csv"
with open(path,"rb") as f:
    encoding = chardet.detect(f.read())["encoding"]

df = pd.read_csv(path,encoding=encoding)

def process_cell(cell):
    if pd.isna(cell):  
        return []
    try:
        result = literal_eval(cell) if isinstance(cell, str) else cell
        return result if isinstance(result, list) else [result]
    except:
        return []  

# 장르 매핑
genre_map = {
    "pop": ["pop","easy listening"],
    "hip hop": ["drill", "trap", "rap", "hip hop"],
    "rock": ["grunge","rock","british invasion","metal","nu metal"],
    "blues": ["doo-wop","blues"],
    "jazz": ["swing","adult standard","jazz"],
    "electronic music": ["house", "synth funk","edm","electronica"],
    "country": ["country"],
    "r&b": ["r&b"],
    "soul": ["soul"],
    "folk": ["folk"],
    "k-pop": ["k-pop","korean"]
}
# 역 매핑: 키워드 -> 장르
keyword_to_genre = {keyword: genre for genre, keywords in genre_map.items() for keyword in keywords}

def assign_genre(cell):
    processed = process_cell(cell)
    for word in processed:
        for keyword, genre in keyword_to_genre.items():
            if keyword in word.lower():  # 키워드가 문자열에 포함되어 있는지 확인
                return genre
    return None  

df["processed_genre"] = df["artist genres"].apply(assign_genre)
df.to_csv("genre_processed.csv")
