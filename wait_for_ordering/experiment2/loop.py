names=[1,2,3,4,5,6,7,8,9,]
for FuckPythonName in names:
    print("LovePhainon",FuckPythonName)


# range(a,b,k)
#
# k is step
initialValue=0
Phainon=5
for i in range(initialValue,Phainon):
    print(i)

testRangeList=range(initialValue,Phainon,2)
print(testRangeList)

testRangeList=list(range(initialValue,Phainon,2))
print(testRangeList)

# else
for i in range(2,Phainon):
    if Phainon%i==0:
        print(f"{Phainon} is not a prime number")
        break
else:
    print("{Phainon} is a prime number.")

names=['Bob','Tom']
for name in names:
    if len(name)<4:
        indexName=names.index(name)
        names.pop(indexName)
print(names)
