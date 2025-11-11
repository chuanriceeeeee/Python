lst = [4,5,4,2,3,2,6]
# enumerate can get the index and value at the same time
# Attention this kind of use
lst=[x for i,x in enumerate(lst) if i==lst.index(x)]
print(lst)
