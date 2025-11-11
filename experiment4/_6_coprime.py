import random as rd

def judge(a,b):
    if a==b:
        print(f"{a} and {b} is coprime number")
        return
    if [x for x in range(2,min(a,b)) if a%x==0 and b%x==0]==[]:
        print(f"{a} and {b} is coprime number")
        return
    print(f"{a} and {b} is not coprime number")
    return
if __name__=="__main__":
    a=rd.randint(0,100)
    b=rd.randint(0,100)
    judge(a,b)
