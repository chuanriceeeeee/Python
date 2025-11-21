#def pre_deal(target_txt:str)->list:
#
#def count_words(target_txt:str)->int:
#
#def count_lines(target_txt:str)->int:
#
from collections import Counter
if __name__ == "__main__":
    sum_lines = 0
    with open("./_4target.txt", mode="w", encoding="utf-8") as in_f:
        in_f.write("Hello, world.\n Wow do you want to solve it? No?\n okay~ ")
    with open("./_4target.txt", mode="r", encoding="utf-8") as in_f:
        for line in in_f:
            sum_lines += 1
    with open("./_4target.txt", mode="r", encoding="utf-8") as in_f:
        target_string = in_f.read()
    target_string = target_string.strip()
    target_list = target_string.split(' ')
    sum_words = len(target_list)
    print(f"Summary lines={sum_lines}\n{sum_words}")
