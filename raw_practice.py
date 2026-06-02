words = ["good", "tree", "bcac"]

result = []

for word in words:

    seen = set()
    unique_word = ""

    for ch in word:

        if ch not in seen:
            unique_word += ch
            seen.add(ch)

    result.append(unique_word)

print(result)
