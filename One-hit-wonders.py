import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


from collections import Counter
df = pd.read_csv("./Data/billboard-hot-100-credited-artists.csv")
target_column = df["artist"]
counter_result = Counter(target_column) #artist당 차트인 트랙 수
counts = counter_result.values() 
count_counts = Counter(counts) #value가 1인 key의 수, 2인 key의 수 ...., 100인 key의 수 ...

dic = {"one-hit":0,"less than five":0,"5 to 10":0,"10 to 50":0,
       "50 to 100":0, "more than 100":0,}
for k,v in count_counts.items():
    if k==1:
        dic["one-hit"] += v
    
    elif k<5:
        dic["less than five"] += v
    elif k <= 10:
        dic["5 to 10"] += v
    elif k<=50:
        dic["10 to 50"] += v 
    elif k<=100:
        dic["50 to 100"] += v 
    else:
        dic["more than 100"] += v

plt.figure(figsize=(12,8))
sns.barplot(x=dic.keys(),y=dic.values(),color="salmon")
plt.tight_layout()
plt.savefig("./plots/bar_onehit")


# plt.figure(figsize=(12,8))
# sns.histplot(x=counts, color = "skyblue")
# plt.xlim(0,200)
# plt.tight_layout()
# plt.xlabel("number of tracks")
# plt.ylabel("number of artists")
# plt.savefig("./plots/hist_one_hit")
# plt.show()
