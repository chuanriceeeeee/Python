# re.split() input more split characters
# 1.lower()
# 2.re.spilt
# 3.strip() won't change the original parameter
# 4.Counter -- return a dictionary
# 5.sorted
import re
from collections import Counter

def word_frequency(text, case_sensitive=False, top_n=None):
    # lower text if false
    if case_sensitive==False:
        # lower() won't change the original text
        text=text.lower()
    #after_text=re.split(r"!|\*|\.|\?|。|,|，| ",text)
    after_text=re.split(r"[!*.?。,， ]",text)

    #O(n**2)
    #after_text=[x for x in after_text  if x.strip()!=' ']
    #[x.strip() for ...] excape ' '
    after_text=[x.strip() for x in after_text  if x.strip()]
    #dictionary=dict([(x,after_text.count(x)) for x in after_text][:top_n])

    dictionary=Counter(after_text)
    #sorted use key default, although value will be used in sort, they will finally be abandoned when pass to dictionary#dictionary=dict(sorted(dictionary,key=lambda x:dictionary[x],reverse=True)[:top_n-1])

    dictionary=sorted(dictionary.items(),key=lambda x:dictionary[x],reverse=True)
    if top_n!=None:
        # [:end] end isn't included!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        dictionary=dictionary[:top_n]
    return dict(dictionary)

if __name__=="__main__":
    text=input("Input a text:\n")
    case_sensitive = False
    sensitive=input("Do you want to lower the parameter?(Y/N)\n")
    # except n\N
    if sensitive.lower()=="n":
        case_sensitive=True
    # except valueError
    try :
        N=int(input("Input the number of the most frequent words you want to return:\n"))
    except ValueError:
        print("Please input a number!")
        exit()

    print(word_frequency(text,case_sensitive,N))