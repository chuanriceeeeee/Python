# len
#
StringInput=input("Input a string:\n")
index=StringInput.rfind(" ")
StringLastWord=StringInput[index:]
StringLastWordLen=len(StringLastWord)-1
print(StringLastWordLen)

