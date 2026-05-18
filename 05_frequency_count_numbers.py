from collections import defaultdict

nums = [1, 2, 1, 3, 2, 1, 0, 0, 0, 0, 45, 0]

"""
Steps : 
  first iterate over a loop
  make a key of every unique number if key exist +=1 in key value 
  now lets try
"""
freq_count = defaultdict(int)
for num in nums:
    # if key exist increment the value else generate a key and value on first seen
    freq_count[num] += 1

print(freq_count)
