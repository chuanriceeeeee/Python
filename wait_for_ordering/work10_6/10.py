ListStr=[]
prefix=[]
while True:
    tempStr=input("Input a string and end input with \"done\":")
    if tempStr=="done":
        break
    ListStr.append(tempStr)
for chars in zip(*ListStr):
    if len(set(chars)) == 1:
        prefix.append(chars[0])  # 加入公共前缀
    else:
        break  # 出现不同字符，终止循环
strTest=''.join(prefix)
print(strTest)
