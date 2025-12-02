import random

List=[random.randint(1,100) for _ in range(20)]
print(f"List:{List}")
ListBefore=sorted(List[:10],reverse=False)
print(f"Prior 10 elements after sorted:{ListBefore}\n")
ListAfter=sorted(List[10:],reverse=True)
print(f"Below 10 elements after sorted:{ListAfter}\n")
