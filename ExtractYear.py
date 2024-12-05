import pandas as pd
chunksize = 10**6
filtered_chunks = []
target_year =  2013
for chunk in pd.read_csv("./year_country_artists.csv", chunksize=chunksize):
    filtered_chunk = chunk[chunk['year'] == target_year]
    filtered_chunks.append(filtered_chunk)

filtered_df = pd.concat(filtered_chunks)
filtered_df.to_csv(f"{target_year}_filtered.csv", index=False)