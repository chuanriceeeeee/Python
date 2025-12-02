# sorted won't change the original tuple
tup=(90,76,85,56,88,70)
TempList=list(tup)
TempList=sorted(tup,reverse=False)

TempList=TempList[2:]
tup2=tuple(TempList)
print(tup2)