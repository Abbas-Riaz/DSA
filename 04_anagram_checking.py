from collections import defaultdict

words = ["cat", "bat", "tac", "tab", "act", "ate", "eat", "tea", "mat"]


""" steps : 
      iterate over words 
      sort the word 
      make sort word key wo se can add every word which is sorted  and add to exact key after sorting 
      at last make a array of values 
    """
dict = defaultdict(list)  #  Create dict where missing keys default to 0
for anagram in words:
    sorted_anagram = "".join(sorted(anagram))

    # create a key of sorted anagram if any anagram is match to sorted key  will added to intended group

    dict[sorted_anagram].append(anagram)
print(dict)
print(dict.values())
