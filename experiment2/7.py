# sum
# len
# max
# values
# keys
# sorted won't change the factor you input, you need assign it to another iterator
# dictionary default iterator is key
# items()
# dict()

mark_math = {'Tom': 86, 'Tony': 91, 'May': 65, 'Bob': 75}
ValueMax=max(mark_math.values())

print("MaxGrade:",ValueMax)

# ListTranslate=sorted(mark_math.items(),key=lambda x:x[1])
ListTranslate=sorted(mark_math.items())

mark_math=dict(ListTranslate)
print(mark_math)

DictionaryLength=len(mark_math)
DictionaryValueTotal=sum(mark_math.values())
AverageValue=DictionaryValueTotal/DictionaryLength
print(f"Average grade is {AverageValue:.2f}")

