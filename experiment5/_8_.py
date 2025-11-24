# os.path.dirname()
# List Tuple:List[int]
import re
import os
from typing import List,Tuple

def string_list(string:str)->list:
    target_list=re.split(r'[,]',string)
    # remove float
    try:
        target_list=[int(x) for x in target_list]
    except ValueError:
        print("Please examinate the file! Not pure number!")
        exit(0)
    return target_list
def sum_equal_target(target_list:list)->list:
    length=len(target_list)
    final_number=target_list[length-1]
    after_list_tuple=[]
    index_x,index_y=0,0
    examine_list=[]
    while index_x<length-1:
        # initialize index_y everytime
        index_y=index_x+1
        while index_y<length-1:
            if index_x not in examine_list and index_y not in examine_list:
                if target_list[index_x]+target_list[index_y]==final_number:
                    after_list_tuple.append((index_x,index_y))
                    examine_list.append(index_x)
                    examine_list.append(index_y)
                    # find then index_x useless:out second loop
                    break
            index_y+=1
        index_x+=1
    return after_list_tuple

def hash_sum_equal_target(target_list:List[int])->List[Tuple[int,int]]:
    length=len(target_list)
    target_value=target_list[length-1]
    #{} intialize dictionary first,set can use set()
    hash_dict={}
    used_indecies=set()
    result=[]
    #construct hash list
    #enumerate generate a tuple (idx,val)
    for idx,val in enumerate(target_list):
        if val not in hash_dict:
            hash_dict[val]=[]
        hash_dict[val].append(idx)
    
    for idx,val in  enumerate(target_list):
        if idx in used_indecies:
            continue

        complement=target_value-val
        if complement not in target_list:
            continue
        
        for complement_idx in hash_dict[complement]:
            if complement_idx!=idx and complement_idx>idx and complement_idx not in used_indecies:
                used_indecies.add(complement_idx)
                used_indecies.add(idx)
                result.append((idx,complement_idx))
                # only use idx once if not break may cause several idx in result
                break
    return result


if __name__=="__main__":
    target_path='./num.txt'
    end_path='./out.txt'
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(script_dir, "num.txt")
    
    with open(target_path,mode="r",encoding="utf-8") as file:
      
        target_string=file.read()
        print(f"target_string:{target_string}")
        after_list=string_list(target_string)
        after_list_tuple=sum_equal_target(after_list)
        after_list_tuple_hash=hash_sum_equal_target(after_list)
    with open("./out.txt",mode="w",encoding="utf-8") as file:
        for x in after_list_tuple:
            file.write(f"{x}")
    with open("./out.txt",mode="r",encoding="utf-8") as file:
        print(file.read())
    
    with open("./out2.txt",mode="w",encoding="utf-8") as file:
        for x in after_list_tuple:
            file.write(f"{x}")
    with open("./out2.txt",mode="r",encoding="utf-8") as file:
        print("hash:\n",file.read())
