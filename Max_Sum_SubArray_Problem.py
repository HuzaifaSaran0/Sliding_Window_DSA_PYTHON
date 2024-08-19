def max_sub_array(arr, k):
    max_sum = 0
    current_sum = 0
    l = 0
    for i in range(0, len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - (k-1)]
    return max_sum

print(max_sub_array([4, 2, 1, 7, 9, 3, 2, 8, 1, 0], 3))
