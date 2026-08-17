from collections import defaultdict

nums = [1, 2, 3, 1, 4, 2, 5]

frequency = defaultdict(int)

# Pass 1: count
for num in nums:
    frequency[num] += 1

# Pass 2: find FIRST unique in original order
for num in nums:
    if frequency[num] == 1:
        print(num)
        break
