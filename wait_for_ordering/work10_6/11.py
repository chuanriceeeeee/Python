strTest=input("Input a string within the length 1000000:\n")

ListstrTest=list(strTest)
LengthStr=len(ListstrTest)
if LengthStr%2==0:
    before=ListstrTest[:int(LengthStr/2)]
    after=ListstrTest[int(LengthStr/2):]

#! here we got a problem
# reverse() won't create a new list but change the element in the oringinal list
# reverse() only return None
# so after=list[:].reverse() only got after==None
    after.reverse()
    if before==after:
        print("True")
    else:
        print("False")
else:
    before=ListstrTest[:int((LengthStr-1)/2)]
    after=ListstrTest[int((LengthStr-1)/2+1):]
    after.reverse()
    if before==after:
        print("True")
    else:
        print("False")


