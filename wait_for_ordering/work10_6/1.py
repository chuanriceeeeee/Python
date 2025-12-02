scoreList=[]

while True:
    temp = input("Enter the score ended with 'done':\n")
    if temp=='done' :
        break
    # remember that input use string type
    scoreList.append(int(temp))
# copy
TestList1=scoreList[:]
# use
scoreList.remove(max(scoreList))
scoreList.remove(min(scoreList))
finalScore=(sum(scoreList))/len(scoreList)
print(f"FinalScore is {finalScore}")

scoreList=TestList1[:]
# don't use
maxValue=scoreList[0]
# find max
temp2=scoreList[0]
for i in scoreList:
    if i>=temp2:
        temp2=i
# find min
temp3=scoreList[0]
for i in scoreList:
    if i<=temp3:
        temp3=i

count=0
sum=0
for x in scoreList:
    sum+=x
    count+=1

sum-=temp3+temp2
avgScore=sum/(count-2)
print(f"FinalScore is {avgScore}")
