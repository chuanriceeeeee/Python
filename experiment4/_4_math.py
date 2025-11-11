#from numpy.ma.extras import average
# *args -- position parameter--don't need name--output tuple
# **kwargs -- key word parameter -- need key=value --output dictionary

import math
def cal_data(mode,*args):
    avg=sum(args)/len(args)
    if mode =="all":
        return (sum(args),avg,max(args),min(args))
    if mode=="sum_max":
        return (sum(args),max(args))
    if mode=="avg_min":
        return(avg,min(args))
    print("Please input at least one number.\n")
    return
if __name__=="__main__":

    mode=input("Please input mode:\n1.all\n2.sum_max\n3.avg_min\n")
    print(cal_data(mode,1,2,3,4,5))