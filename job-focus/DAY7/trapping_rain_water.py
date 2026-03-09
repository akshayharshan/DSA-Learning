def trapping_rain_water(height):

    left_wall = 0
    right_wall = 0

    max_left = [0] * len(height)
    max_right = [0] * len(height)

    for i in range(len(height)):
        j = -i-1
        max_left[i] = left_wall
        max_right[j] = right_wall

        left_wall = max(left_wall,height[i])
        right_wall = max(right_wall,height[j])
    
    water = 0
    for i in range(len(height)):
        min_height = min(max_left[i],max_right[i])
        water_contain = min_height - height[i]
        if water_contain >= 0:
            water+=water_contain

    return water






print(trapping_rain_water([4,2,0,3,2,5]))


