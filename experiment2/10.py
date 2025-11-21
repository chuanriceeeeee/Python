nums = [10, 23, 5, 7, 12, 18, 3, 16]
new_nums1=[x*2 for x in nums ]
print(new_nums1)
new_nums = [x * 2 if x % 2 == 0 else x + 1 for x in nums]
print(new_nums)
