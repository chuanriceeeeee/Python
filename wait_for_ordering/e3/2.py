import random
N=int(input("Input N as the number of random integer:\n"))
List=[random.randint(1,1000) for _ in range(N)]
for _ in List:
    Temp=List.count(_)
    TempValue=_
    if Temp!=1:
        while Temp!=1:
            List.remove(TempValue)
            Temp-=1
List.sort(reverse=False)
print(List)