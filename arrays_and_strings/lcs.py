

def longest_common_subsequence(s1, s2):
    rows, cols = len(s1)+1, len(s2)+1

    dp = [[0 for i in range(cols)] for j in range(rows)]
    dp[0][0] = 0

    for row in range(rows):
        for col in range(cols):
            if (row == 0 and col != 0) or (col == 0 and row != 0):
                dp[row][col] = 0
                continue
            if s1[row-1] == s2[col-1]:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col]) + 1
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col])

    return dp[rows-1][cols-1]


print(longest_common_subsequence("abcdaf", "acbcf"))
print(longest_common_subsequence("Brijesh", "Brij"))
print(longest_common_subsequence("Brijesh", "Mukti"))
print(longest_common_subsequence("Brijesh", "Patel"))
