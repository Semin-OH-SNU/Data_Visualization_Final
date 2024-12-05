import pandas as pd
"""csv파일의 특정 열에 대해 unique한 값만을 가져와서 저장하는 모듈"""

# #데이터 형식 str일 경우.
# df = pd.read_csv("./year_country_artists.csv")
# unique_values = df["artists"].unique() #대상 열 지정
# unique_df = pd.DataFrame({"Unique Values": unique_values})
# unique_df.to_csv("unique_artists.csv", index=False)

# #데이터 형식 list(str,str,..,str)일 경우.
# df = pd.read_csv("./2023_filtered.csv")
# df['unique_artists'] = df['artists'].apply(eval)
# all_items = [item for sublist in df['unique_artists'] for item in sublist]
# unique_values = list(set(all_items))
# unique_df = pd.DataFrame({'unique_artists': unique_values})
# unique_df.to_csv("unique_artists_2023.csv", index=False)
