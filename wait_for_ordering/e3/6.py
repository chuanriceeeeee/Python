lst = [12,6,4,1,8,2,5,1,8,9,10,15,18,22]
sum_lst=[sum(lst[lst.index(x):lst.index(x)+3]) for x in lst if lst.index(x)%3==0]
print(sum_lst)