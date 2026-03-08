def most_water_container(height):

    left = 0
    right = len(height) -1
    max_area = 0

    while left < right:
        width = right - left
        length = min (height[left],height[right])
        max_area = max(width * length, max_area)
        if height[left] < height[right]:
            left+=1
        else:
            right -=1
    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(most_water_container(height))



