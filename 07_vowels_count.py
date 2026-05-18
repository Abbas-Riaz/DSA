s = "programming"
vowel_count = 0
# taking sets for checking each letter is in vowels or not
vowels = {"a", "e", "i", "o", "u"}
for letter in s:
    if letter in vowels:
        vowel_count += 1
# result of how many vowels are there
print(vowel_count)
