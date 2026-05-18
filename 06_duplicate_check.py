nums = [1, 1, 2, 3, 4, 1, 4]

dict = {}

"""Steps
    for dup check first make a key of a number 
    if key exist value duplicate else add a new key 

"""

for num in nums:

    if num in dict:
        if dict[num] != "duplicate":
            dict[num].append("duplicate")
    else:
        dict[num] = []
print(dict)
