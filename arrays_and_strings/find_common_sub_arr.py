
arr1 = [5]
arr2 = [5, 6, 1, 2, 3, 4, 8, 1, 2, 9, 8]

def find_common_sub_array(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return 0
    long_arr = arr1 if len(arr1) >  len(arr2) else arr2
    short_arr = arr2 if len(arr1) > len(arr2) else arr1
    
    dp = [[0 for _ in range(len(short_arr))] for _ in range(len(long_arr))]
    
    for i in range(len(long_arr)):
        for j in range(len(short_arr)):
            if long_arr[i] == short_arr[j]:
                dp[i][j] += dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

    max_length = 0
    for i in range(len(dp)):
        max_length = max(max_length, max(dp[i]))
    
    return max_length



print(find_common_sub_array(arr1, arr2))