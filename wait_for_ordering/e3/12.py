def NotTwice(indexB,Used_indices):
    if indexB in Used_indices:
        return False
    else:
        return True

nums=input("nums=(Eg:1,2,4,6):\n").strip() # strip--remove the empty character before and after the string
target=int(input("target=(Eg:9):\n"))

NumsList = [int(num.strip()) for num in nums.split(',')]

LengthNums=len(NumsList)

indexA=0
NumsTarget=[]
Used_indices=[]
while indexA<LengthNums-1:
    indexB=indexA+1
    while indexB<LengthNums:
        if NumsList[indexA]+NumsList[indexB]==target and NotTwice(indexB,Used_indices) and NotTwice(indexA,Used_indices): 
            NumsTarget.append([indexA,indexB])
            Used_indices.append([indexB,indexA])
            break
        indexB+=1
    indexA+=1
for i in NumsTarget:
    print(i,"\n")