def showup_max(lst):
    return max([(x,lst.count(x)) for x in lst ],key=lambda x:x[1])  # max only return one parameter!! what if there is more?
if __name__=="__main__":
    lst = [2, 2, 3, 1, 2, 2, 1, 8, 5]
    print(f"Maximum show-up number is {showup_max(lst)[0]}.")
