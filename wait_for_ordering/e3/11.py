AString=input("Input String A\n")
BString=input("Input String B\n")
TestStr=set(AString)&set(BString)

# !!!
AString=[char if char not in TestStr else "_" for char in AString]
BString=[char if char not in TestStr else "_" for char in BString]
AString=''.join(AString)
BString=''.join(BString)

print(AString,"\n")
print(BString,"\n")