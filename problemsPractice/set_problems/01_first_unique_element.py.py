nums = [4, 7, 2, 7, 9, 4, 1]

# set for keeping record while iterating

seen = set()


for num in nums:
    if num in seen:
        print(f" {num } is first duplicati")
        break
    seen.add(num)
