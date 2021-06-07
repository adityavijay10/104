import csv
from collections import Counter

with open('./SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_nun=file_data[i][1]
    new_data.append(float(n_nun))

#finding mean
n=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/n
print('mean: ',str(mean))

#finding median
new_data.sort()
if(n%2==0):
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2

else:
    median=float(new_data[n//2])

print('median: ',str(median))

#finding mode

data=Counter(new_data)
modeDataForRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}

for height,occurence in data.items():
    if(50<float(height)<60):
        modeDataForRange['50-60']+=occurence
    elif(60<float(height)<70):
        modeDataForRange['60-70']+=occurence
    elif(70<float(height)<80):
        modeDataForRange['70-80']+=occurence

modeRange,modeOccurence=0,0

for range ,occurence in modeDataForRange.items():
    if(occurence>modeOccurence):
        modeRange,modeOccurence=[int(range.split("-")[0]), int(range.split("-")[1])],occurence

mode=float((modeRange[0]+modeRange[1])/2)
print('mode: ',str(mode))