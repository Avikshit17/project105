import pandas as pd
import math
df=pd.read_csv("class1.csv")
marks=df["Marks"].tolist()
sum=0
for eachdata in marks:
    sum=sum+int(eachdata)
mean=sum/len(marks)
sum=0
for eachdata in marks:
    sub=int(eachdata)-mean
    sq=sub**2
    sum=sum+sq
result=sum/(len(marks)-1)
std=math.sqrt(result)
print(std)


