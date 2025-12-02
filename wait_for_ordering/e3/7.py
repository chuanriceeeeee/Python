lst = [4,5,4,2,3,2,6]
# if you del element in 'for' loop, it will cause index unavailable
tempIndex=0
while (tempIndex+1)<len(lst):
    tempElement=lst[tempIndex]
    tempIndex2=tempIndex+1
    while tempIndex2<len(lst):
        if lst[tempIndex2]==tempElement:
            del lst[tempIndex2]
            tempIndex2-=1
        tempIndex2+=1
    tempIndex+=1
#for _ in lst:
#    count=lst.count(_)
#    if count >1:
#        # lst[index].index() is unavailable
#        index=lst[lst.index(_)+1:]
#        del lst[lst.index(index)]
print(lst)
