"""
Implement an algorithm to determine if string has all unique characters. what if you can not use additional data
structure?
"""


# def is_unique(word):
#     chars = [False] * 128
#     for item in word:
#         if not chars[ord(item) - ord('a')]:
#             chars[ord(item) - ord('a')] = True
#         else:
#             return False
#     return True

def is_unique(word):
    if len(word) <= 1:
        return True
    for i in range(0, len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return False
    return True


print(is_unique("878"))
