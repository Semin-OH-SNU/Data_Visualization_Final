import pandas as pd

# CSV 파일 읽기
filtered_df = pd.read_csv("./2023_filtered.csv")
unique_df = pd.read_csv("./unique_artists_with_country.csv")

filtered_df['artists_country'] = None

# unique_artists를 키로, country를 값으로 하는 딕셔너리 생성
artist_country_map = unique_df.set_index("unique_artists")["country"].to_dict()

# artists 열의 리스트에서 unique_artists와 매칭되는 country 찾기
def map_country(artists_list, artist_country_map):
    for artist in eval(artists_list):  # 문자열로 저장된 리스트 평가
        if artist in artist_country_map:
            return artist_country_map[artist]
    return None

# artists_country 열에 데이터 저장
filtered_df['artists_country'] = filtered_df['artists'].apply(
    lambda x: map_country(x, artist_country_map)
)

# 결과 저장
filtered_df.to_csv("./2023_filtered.csv", index=False)
