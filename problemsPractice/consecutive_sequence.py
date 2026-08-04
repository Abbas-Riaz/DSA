nums = [100, 4, 200, 1, 3, 2]


numbers = set(nums)

longest = 0


for num in nums:

    if num - 1 not in numbers:

        current_num = num
        current_length = 1

    while current_num + 1 in numbers:
        current_num += 1
        current_length += 1

    if current_length > longest:
        longest = current_length

print(longest)
