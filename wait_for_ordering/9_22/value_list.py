a=1000000000000
c=1000000000000
print(id(a))
print(id(c))
b=a
print(id(a))
print(id(b))
## list
list2=[1,2,3,4,5]
list3=list2[:2]
print(list3)
## list[start: end:step]
## step>0 means it divided from left to right
## ignore step means step default 1
## end is the mark !!!before the true end
list4=list2[::-1]
list5=list2[::]
print("4",list4)
print("5",list5)

list6=list2[-1:-6:-1]
print(list6)


## sorted(iterable, key=None, reverse=False)
## iterable:the iterable object you want to sort(list,tuple,str)
## key reliable of compare
## default:False:up                  True:down
numbers=[1,6,5,3,135,2222222222,134354263243474,745354351342]
numbers=sorted(numbers,reverse=True) ## sorted create a new list
print("reserved",numbers)

## reversed(seq)\
## return a iterator
## need a constraint transport


## some other function inside list
list2.append(496)
print(list(["tip1"])+list2)
list2.pop(1)
print(list2)
## since Error come out, it won't run the rest of code.It will search the Error Type in except
try:
    RemoveValue1=input("Please input the value you want to delete in this list:\n")
    list2.remove(int(RemoveValue1))
    print("Delete successfully!")
except ValueError:
    print(f"There isn't a element {RemoveValue1} in the list")

## reverse
## turn the whole list a round
## it will change the list directly and return nothing
list2.reverse()
print(list2)

## a,*b=1,2,3,4,5
a,*b=1,2,3,4,5
print(f"type b is type(b)")


## tuple
test_tuple2=(1,)
print(type(test_tuple2))

## tuple packaging and tuple unpacking



Test_tuple_a,Test_tuple_b,Test_tuple_c=(1,2,3)
print(Test_tuple_a,Test_tuple_b,Test_tuple_c)


## input
## default input valuable type is "string"
