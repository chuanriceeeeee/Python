FindStr='Python'
TargetStr='Python is great. I love Python. Python\'s syntax is simple. Learn Python today!'
TestStr=''
index=0
CountNumber=0
while True:
    index=TargetStr.find(FindStr)
    if index==-1:
        break
    else:
        TargetStr=TargetStr[index+len(FindStr):] # index is less than FindStr at the first time, and if you need move you need use plus
        CountNumber+=1
print(f"The key word\"Python\" has shown for {CountNumber} times.")