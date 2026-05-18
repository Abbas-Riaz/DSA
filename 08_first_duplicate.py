nums = [4, 2, 7, 4, 9, 2]

"""
steps : 
    as we are checking first duplicate 
    iterate over nums
    append or create dic key for each num we are iterating with default value is false
    check each num if value is false make it true and break  
"""

from collections import defaultdict

duplicates = defaultdict(list)
first_duplicate = None

for is_duplicate in nums:

    if duplicates[is_duplicate]:
        first_duplicate = is_duplicate
        break

    else:
        duplicates[is_duplicate] = True


print(first_duplicate)
