scores=[85,92,78,65,90,88]
sum=0
for i in scores:
    sum+=i
Avg=sum/len(scores)
print(f"Average score is {Avg}")

print(f"Minimum score is {min(scores)}")
print(f"Maximum score is {max(scores)}")
print(sorted(scores,reverse=True))
Insert=82
scores.append(Insert)
print(scores)