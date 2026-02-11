def most_water(height):
    l=0
    r = len(height) -1
    max_area = 0
    while l < r:
        area = (r-l)*min(height[l],height[r])
        max_area = max(area,max_area)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return max_area






height = [1, 1]
print(most_water(height))