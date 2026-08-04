s = "abcadefgh"

seen = set()
left = 0
max_len = 0

for right in range(len(s)): # iterating over string 

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    current_len = right - left + 1

    if current_len > max_len:
        max_len = current_len

print(max_len)
