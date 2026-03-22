def container_with_most_water(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left < right:
        width = right - left
        area = width * min(heights[left],heights[right])
        max_area = max(area,max_area)
        if heights[left] <= heights[right]:
            left +=1
        else:
            right -=1
    return max_area

height = [0,2,0,4,0]
print(container_with_most_water(height))