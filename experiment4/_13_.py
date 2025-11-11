# 对于join，前提条件是list中都是字符串
def isPrime(num:int)->bool:
    if len([x for x in range(2,num) if (num)%x==0])==0:
        return True
    else:
        return False
def isLoopPrime(num):
    if isPrime(num):
        length=len(str(num))
        list_num=[]
        for _ in range(length-1):
            num=num//10+(num%10)*(10**(length-1))
            list_num.append(num)
# num have already been examinated
        if len([x for x in list_num if isPrime(x)==False])==0:
            return True
    return False
if __name__=="__main__":
    while True:
        try :
            range_num=int(input("Input target number over 10 and under or equal to 2000:\n"))
            while (range_num>10 and range_num<=2000)==False:
                range_num = int(input("Input target number over 10 and under or equal to 2000:\n"))
        except ValueError:
            print("Please input a integer!\n")
            continue
        break
    list_num=[x for x in range(2,range_num+1) if isLoopPrime(x)]
    print(list_num)