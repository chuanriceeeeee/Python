from collections import Counter
# Counter O(n) count O(n^2)

str=input("Paste or input your string:\n")

# data pre deal
# lower will create a new string
str=str.lower()
Strlist=''

for i in str:
    if i.isspace() or i.isalpha():
        Strlist+=i
strTranslate=Strlist.split()

listTest={'of','a','an','the'}
RestrTranslate=[i for i in strTranslate if i not in listTest]

StoreDic={}

word_counts=Counter(RestrTranslate) # Counter({'apple': 3, 'banana': 2, 'orange': 1}) output counter object
Output=[word for word ,count in word_counts.items()if count>2]
print(Output)



    