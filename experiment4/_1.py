# 四叶草数--四次方幂相加
def exmainate_water_flower_num(minimum,maximum):
    after_exam=[]
    after_exam=[x  for x in range(minimum,maximum) if (x//100)**3+(x//10-x//100*10)**3 + (x%10)**3 ==x]  # ** instead of bitwise operators ^
    for _ in after_exam:
        print(_)
    return after_exam


if __name__=="__main__":  # main function judgement
    minimum=int(input("Input the minimum number:\n"))
    while minimum<100:
        print("Please input the three-digit number!\n")
        minimum=int(input("Input the minimum number:\n"))
        

    maximum=int(input("Input the maximum number:\n"))
    
    while maximum<=minimum:
        print("Please input a number bigger than minimum number!\n")
        minimum=int(input("Input the maximum number:\n"))
    
    exmainate_water_flower_num(minimum,maximum)
