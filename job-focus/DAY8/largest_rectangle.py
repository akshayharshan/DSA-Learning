def largest_rectangle(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            index,height = stack.pop()
            max_area = max(max_area,height * (i - index))
            start = index
        stack.append((start,heights[i]))
    for i,h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

heights = [2,1,5,6,2,3]
print(largest_rectangle(heights))
            