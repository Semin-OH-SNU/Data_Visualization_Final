import pandas as pd
import requests
import time
import os

"""
unique_artists_(year).csv파일에 저장된 각 artists에 대해,
MUsicBrainz API에 artist명으로 qeury 요청
아티스트의 국가 데이터를 가져와 저장"""

BASE_URL = "https://musicbrainz.org/ws/2/artist/"
CHECKPOINT_FILE = "unique_artists_with_country.csv" #임시 저장 파일

#"artist"열의 문자열로 쿼리 요청, 응답 데이터 중 country값을 return
def get_artist_country(artist_name):
    headers = {"User-Agent": "Data_Visualization_Practice/1.0 (dhtpals@snu.ac.kr)"}
    params = {
        "query": artist_name,
        "fmt": "json",
    }
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if "artists" in data and len(data["artists"]) > 0:
            artist_info = data["artists"][0]
            if "country" in artist_info:
                return artist_info["country"]  
        return "Unknown" 
    except Exception as e:
        print(f"Error fetching data for {artist_name}: {e}")
        return "Error"


if os.path.exists(CHECKPOINT_FILE):
    df = pd.read_csv(CHECKPOINT_FILE)
    print("Checkpoint loaded.")
else:
    df = pd.read_csv("unique_artists_2023.csv")
    df["country"] = None 

for idx, row in df.iterrows():
    if pd.notna(row["country"]):  
        continue

    artist_name = row["unique_artists"]
    country = get_artist_country(artist_name)
    df.at[idx, "country"] = country

    # 100행마다 중간 저장
    if idx % 100 == 0:
        df.to_csv(CHECKPOINT_FILE, index=False)
        print(f"Checkpoint saved at row {idx}.")

    # API 요청 간 딜레이 부여.
    time.sleep(1)

# 최종 데이터 저장
df.to_csv(CHECKPOINT_FILE, index=False)

