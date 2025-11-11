from sympy import false


def prime_number(target):
    # []!=None
    if len([x for x in range(2, target) if target % x == 0]) == 0:
        return True
    return False
def goldbach_conjecture(target_number):
    # get the prime number before target_number
    prime_number_list=[x for x in range(1,target_number) if prime_number(x)]
    list_final=[]
    for x in prime_number_list:
        for y in prime_number_list:
            if x+y==target_number:
                list_final.append((x,y))
    if len(list_final)!=0:
        print("Yes")
        for _ in list_final:
            print(f"{target_number}={_[0]}+{_[1]}")
    else:
        print("No")
    return list_final
if __name__=="__main__":
    try_flag=1
    try :
        """
        while in try can still avoid ValueError
        """
        target_number=int(input("Input an even integer:\n"))
        while(target_number%2!=0):
            print("Please input an even integer!\n")
            target_number = int(input("Input an even integer:\n"))

    except ValueError:
        while(try_flag==1 or target_number%2!=0):
            print("Please input an even integer!\n")
            try:
                target_number = int(input("Input an even integer:\n"))
            except ValueError:
                continue
            try_flag=0
    goldbach_conjecture(target_number)
