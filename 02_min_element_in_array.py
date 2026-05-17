nums = [3, 10, 6, 2, 8]

min = nums[0]
for num in nums:
    if num < min:
        min = num


print(f"the min element is {min}")
