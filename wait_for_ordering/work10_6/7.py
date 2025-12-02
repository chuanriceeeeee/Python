PassWordList=[]
index = 0
TranslatedPassWord=0
print("")
while True:
    temp=input("input the password book ended with 'done':\n")
    if temp=='done':
        break
    else:
        try :
            temp=int(temp)
        except ValueError as e:
            print("Please input a integer!\n")
            continue
    PassWordList.append(temp)
PassWordList.sort(reverse=False)
Key=int(input("input electric key:\n"))
for i in PassWordList:
    if Key>i:
        index=PassWordList.index(i)
Before=Key-PassWordList[index]
After=PassWordList[index+1]-Key
if Before>After:
    TranslatedPassWord = PassWordList[index+1]
elif After>Before:
    TranslatedPassWord=PassWordList[index]
else:
    TranslatedPassWord=PassWordList[index]
print(f"Your password have been translated to {TranslatedPassWord} successfully!")
