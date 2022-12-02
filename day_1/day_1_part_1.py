import re
input_nums = open("day_1\input.txt")

nums = []
baskets = [[]]

global_total = 0

for line in input_nums:
    nums.append(re.sub("\n", "", line))
    
input_nums.close()

n = 0
while n < len(nums) - 1:
    try:
        baskets[-1].append(int(nums[n]))
    except ValueError:
        baskets.append([])
    
    n += 1

for basket in baskets:
    total = 0
    for b in basket:
        total += b
    
    if total > global_total:
        global_total = total

print(nums)
print(baskets)

print(global_total)