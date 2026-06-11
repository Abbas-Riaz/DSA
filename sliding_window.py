"""
when we see problem like
    subarray
    substring
    continuous
    consecutive
    window
    longest
    smallest
    maximum
    minimum

"""

nums = [2, 1, 5, 1, 3, 2]
k = 3

# calculate the sum of first three element

window_sum = 0

for i in range(k):
    window_sum += nums[i]
max_sum = window_sum
# now remove first element from from array and add next elment and check if window sum is greater than previous

for i in range(
    k, len(nums)
):  # upto k we have already sum so now we have to remove previous first element of k size array while moving and add next elemeent

    outgoing = nums[
        i - k
    ]  # every time i will increase and we will remove the k element from subarray
    incoming = nums[i]  # as i iterate we will add the next element
    window_sum += -outgoing + incoming

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)
