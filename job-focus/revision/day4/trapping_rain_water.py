def trapping_rain_water(height):
    left_height = [0] * len(height)
    right_height = [0] * len(height)
    l_wall = 0
    r_wall = 0
    
    for i in range(len(height)):
        j = -1-i
        
        left_height[i] = l_wall
        right_height[j] = r_wall

        l_wall = max(l_wall,height[i])
        r_wall = max (r_wall,height[j])
    
    water_capacity = 0
    for i in range(len(height)):

            unit_water = min(left_height[i],right_height[i]) - height[i]
            if unit_water > 0:
                 water_capacity += unit_water
    return water_capacity





height = [2,0,2]
print(trapping_rain_water(height))