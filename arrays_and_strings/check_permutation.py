"""
Given two strings, write a method to decide if one is permutation of other.
"""


def permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = [0] * 128

    for elem in str1:
        array_index = ord(elem) - ord('a')
        chars[array_index] += 1

    for elem in str2:
        array_index = ord(elem) - ord('a')
        chars[array_index] -= 1
        if chars[array_index] < 0:
            return False
    return True


print(permutation("abc", "adf"))
