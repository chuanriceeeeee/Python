import math
def mySum(a,b):
    summarize_num=sum([x for x in range(int(math.ceil(a)),int(math.ceil(b)))])  # sum need translate a iterator
    return summarize_num
if __name__=="__main__":
    # input return string!!!
    a=float(input("Input minimum number:\n"))
    b=float(input("Input maximum number:\n"))
    while b<a:
        print("Please input a number bigger than minimum number!\n")
        b=float(input("Input the maximum number:\n"))
    summarize_num=mySum(a,b)
    print(f"Summarized number is {summarize_num}")

