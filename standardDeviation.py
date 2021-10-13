import csv
import math
f=open("data.csv")
reader=csv.reader(f)
filedata=list(reader)

data=filedata[0]
sum=0
for eachdata in data:
    sum=sum+int(eachdata)
mean=sum/len(data)
sum=0
for eachdata in data:
    sub=int(eachdata)-mean
    sq=sub**2
    sum=sum+sq
result=sum/(len(data)-1)
std=math.sqrt(result)
print(std)
