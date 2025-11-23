import re
from collections import Counter
word_list = [ "artificial", "intelligence", "machine", "learning", "deep", "models", "algorithms", "data", "systems", "recognition", "speech", "image", "neural", "networks", "ethical", "challenges", "future", "research", "development", "business"]

def pre_operate(target_string:str)->dict:
    target_string=target_string.lower()
    target_string_list=re.split(r"[!,?*. ]",target_string)
    target_string_list=[x.strip() for x in target_string_list if x.strip()]
    target_string_list=[x for x in target_string_list if x in word_list]
    target_string_dict=Counter(target_string_list)
    
    return dict(target_string_dict)
if __name__=="__main__":
    target_path="./test.txt"
    with open(target_path,mode="r",encoding="utf-8") as file:
        frequency_dict=pre_operate(file.read())
        print(frequency_dict);
