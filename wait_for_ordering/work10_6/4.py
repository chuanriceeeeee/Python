Str1=input("Input the word 1:\n")
Str2=input("Input the word 2:\n")

# translate it to list and use set to compare
# & is a function in set to find the same element
# and is equal to && in c++
if len(Str1)==len(Str2) and (sorted(Str1)==sorted(Str2)):
    print("They are each other's anagram.")
else:
    print("They aren't anagrams")
