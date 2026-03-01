def water_trap(heights):
    left_wal, right_wal = 0,0
    n = len(heights)
    water = 0

    max_left = [0] * n
    max_right = [0] * n

    for i in range(n):
        j = -i-1    
        max_left[i] = left_wal
        max_right[j] = right_wal

        left_wal = max(left_wal,heights[i])
        right_wal = max(right_wal,heights[j])

    for i in range(n):

        pot = min(max_left[i],max_right[i])
        water += max(0,pot - heights[i])

    return water


nums =[0,1,0,2,1,0,1,3,2,1,2,1]
print(water_trap(nums))

