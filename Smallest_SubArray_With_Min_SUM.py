def smallest(arr, target):
    current_wind_sum = 0
    min_wind_sum = (2**31)-1
    start_wind = 0
    for end_wind in range(len(arr)):
        current_wind_sum += arr[end_wind]
        while current_wind_sum >= target:
            min_wind_sum = min(min_wind_sum, end_wind - start_wind + 1)
            # "windEnd - windStart + 1"
            # This is To Get the size of current Window
            current_wind_sum -= arr[start_wind]
            start_wind += 1
            # currentWindSum -= arr[windStart]; 
            # This is To Shrink the Current Window from Left 
        
    return min_wind_sum

print(smallest([3,2,5,6,7,8,3,6,7,3], 8)) # 1
