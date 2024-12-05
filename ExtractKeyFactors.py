import pandas as pd
import chardet


path = ".\Data\prepared.csv"
with open(path,"rb") as f:
    encoding = chardet.detect(f.read())["encoding"]

df = pd.read_csv(path,encoding=encoding)
meta_category = ["year","titles","rank"]
artist_category = ["year","artist name","artist genres","artist popularity"]
track_category = ["year","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","valence","tempo","duration ms","time signature"]

meta_df = df[meta_category] #year, song titles, belonging album
artist_df = df[artist_category] #year + artist name, genres, popularity 
track_df = df[track_category] #year + audio_features of each tracks

""" Description for each track category
danceability : 댄스음악인가? scale: 0.0 - 1.0. larger, danceable
acousticness: acoustic한 정도. 즉, 전자음이 들어간 정도. scale: 0.0-1.0. larger, acoustic.
energy : energetic? scale:0.0 - 1.0. larger, energetic(fast, fancy, noisy)
key: pitch. scale -1-11. using standard Pitch Class Notation
instrumentlness : 악기의 비중. scale: 0.0 - 1.0. larger, less vocal
liveness : 음원 상에 청중의 존재가 느껴지는 정도. scale: 0.0-1.0. 0.8이상이면 라이브 음원.
loudness : 트랙의 총 데시벨. scale: -60 ~ 0dB.
mode : major(장조) = 1, minor(단조) = 0
speechiness : 'spoken word'의 비중; scale 0.0-1.0; 0.6 이상은 팟캐스트; 0.3-0.6: 랩; 0.3 미만: 랩 이외의 음악 
tempo : 템포, scale:real-scale. beats per minute(BPM).
valence : valence 음악에서 느껴지는 정서. scale: 0.0-1.0. larger, positive
"""