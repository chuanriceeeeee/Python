str=input("Input a string construct with letters, number, and space with a character:\n")
List=list(str)
# start from 0!!!!
ListSplit=List[:len(List)-1]
targetCharacter=List[len(List)-1]
print(ListSplit.count(targetCharacter))
