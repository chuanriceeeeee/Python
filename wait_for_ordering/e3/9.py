def primeInteger(InputInteger):
    testIndex=0
    for i in range(2,InputInteger): # not 1. because 1 is every integer's factor
        if InputInteger%i==0:
            testIndex=1
            break
    if testIndex==1:
        return False
    else:
        return True

PositiveInteger=int(input("Input a positive integer:\n"))
Tuplelist=[]
for i in range(1,int(PositiveInteger/2)): # reduce the cost
    if primeInteger(i):
        N=i
        while N<PositiveInteger:
            if primeInteger(N) and N+i==PositiveInteger:
                Tuplelist.append((i,N))  # restore as tuple
            N+=1
for i in Tuplelist:
    print(f"{i}\n")
print(len(Tuplelist))