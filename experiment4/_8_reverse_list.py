def reverse_list(lst,k):
    lst1=sorted(lst,reverse=True)
    return lst1[len(lst) - k:]+lst1[:k]

if __name__=="__main__":
    list=[1,2,3,4,5,6,7,8]
    print(reverse_list(list,4))
