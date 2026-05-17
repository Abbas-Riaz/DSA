nums = [3, 10, 6, 2, 8]

# check if 5 exists in array


for num in nums:
    if num == 5:
        print("5 exists ")
        break
    else:
        print("5 not exists ")
""" count how many even numbers exist """
even_count = 0
for num in nums:
    if num % 2 == 0:

        even_count += 1

print(f"the total even numbers are {even_count}")

""" use of state varialbe 
    """
