nums = [2, 7, 11, 15]
target = 9
numbers = {2, 7, 11, 15}
"""
Steps : 
  consider each iterating element as first element 
  the iterate over list subtract the element from result and check if this element is in set 
"""
dict = {}
for element in nums:
    dict[element] = [element]
for num in nums:
    pair_element = target - num

    if pair_element in dict:
        dict[pair_element].append(num)
        break
print(dict[pair_element])


nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    needed = target - num

    if needed in seen:
        print([seen[needed], i])
        break

    seen[num] = i


nums = [2, 7, 11, 15]
target = 9

seen = {}


for i, num in enumerate(nums):
    needed = target - num

    if needed in seen:
        print([seen[needed], i])
        break
    seen[num] = i
