# dictionary
# dict.fromkeys(seq[,value])
# seq is a sequence, value can set the sequence's value

# from python3.6 dictionary will output a order output
# but attention! this order is only output
# in memory, it won't be orderable


# dic{"A":"C","Apple":"Banana","Orange":"Strawberry"
# key need to be unique and can't be changed
#  string,tuple... can ,but list can't
# create a empty dictionary

# value can be everything and repeatable
d={}
empty={"for":"you"}
empty2=empty
print(id(empty2))
print(id(empty))


# del
try:
    DeleteDictionaryKey=input("Input the key you want to delete:\n")
    del empty[DeleteDictionaryKey]
    print(empty)
except KeyError:
    print(f"{DeleteDictionaryKey} isn't in this dictionary.")

# dict.get(key,default=None)
# it will get the
# default: if the key isn't in this dictionary, it will return None
addressbook={"name":"Tom","Phone":"23456"}


# keys


# items
# it will return a tuple array with list format
# dict_items([('name', 'Tom'), ('Phone', '23456')])
list2=addressbook.items()
print(list2)

# pop()

# popitem()
## return the last input dictionary key-value


## update()