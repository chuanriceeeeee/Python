import string

lowercase = string.ascii_lowercase

lowercase+=lowercase

letter=input('Input the letter:\n')
AfterEncrypt = lowercase[lowercase.index(letter)+4]
print(f'{AfterEncrypt}')

