lst = [4, 5, 4, 2, 3, 2, 6]
seen = set()  
result = []

for num in lst:
    if num not in seen:
        seen.add(num)    
        result.append(num) 

print(result) 
