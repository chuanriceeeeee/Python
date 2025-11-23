# str.split() only fit seperate string with space' ', 
# if you need to translate string to list letter by letter, you just need to list()
# by the way, every function with string won't consider the number of exterminal character

import os
supported_file=['docx','doc','pdf','txt']
def is_supported(target_str:str)->bool:
    target_str=target_str.lower()
    print(len(target_str))
    target_str_list=list(target_str)
    target_str=''.join(target_str_list[target_str.rfind('.')+1:])
    if target_str in supported_file:
        return True
    else:
        return False
if __name__=="__main__":
    target_path="./file1.txt"
    if os.path.exists(target_path):
        with open("./file1.txt",mode="r",encoding="utf-8") as file:
            if is_supported(file.name):
                print("Supported!")
            else:
                print("Not supported!")

    else:
        print(f"{target_path} dosen't exist!\n")