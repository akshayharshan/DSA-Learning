def water_trap(heights):
    l_wall,r_wall = 0,0
    n = len(heights)
    max_left = [0] *n
    max_right = [0] *n
    for i in range(n):
        j = -i-1
        max_left[i] = l_wall
        max_right[j] = r_wall

        l_wall = max(l_wall,heights[i])
        r_wall = max(r_wall,heights[j])
    
    sum = 0

    for i in range(n):
        pot = min(max_left[i],max_right[i])

        sum += max(0, pot - heights[i])


    return sum


nums =[0,1,0,2,1,0,1,3,2,1,2,1]
print(water_trap(nums))