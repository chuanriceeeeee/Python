## find(str,beg=0,end=len(string))
## beg index start end index end before it
filename="example.txt"
print(filename[filename.find('.')+1:]) ## notice!! need plus 1
## rfind（str,）
## find the last you need to find
print(filename[filename.rfind('.')+1:])
## count
## count numbers of one son-string present times


## replace(old,new[,count])
## it will return a new string and won't change the old string

## split
## return a list
letters=filename.split("e")
print(letters)


## join(iterable)
## iterable can be list, tuple and string
jon2="-".join(filename)
print(jon2)