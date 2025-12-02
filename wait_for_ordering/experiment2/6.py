StringInt=input("Input a non-negative integer within the range of a long integer:\n")

StringIntList=list(StringInt)[::-1]
StringIntList=" ".join(StringIntList)
print(StringIntList)