values = [89,70,76,98,72]
limit = 80
for i in range(len(values)-1,-1,-1):
    if values[i] < limit:
        values.pop(i)
print(values)