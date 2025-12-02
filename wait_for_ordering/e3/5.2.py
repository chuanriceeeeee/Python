values = [89,70,76,98,72]
index=0
# here index need to < but not <=
while index<len(values):
    if values[index]<80:
        values.remove(values[index])
        continue
    else:
        index+=1
print(values)