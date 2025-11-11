def same(L1,L2):
    return list(set(L1)&set(L2))
if __name__=="__main__":
    L1=[1,2,3,4,5,6]
    L2=[2,3,4,5,6,7]
    print(same(L1,L2))
