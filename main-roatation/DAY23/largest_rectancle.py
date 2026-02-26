def largest_rectangle(heights):

    heights.append(0)
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            top = stack.pop()
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            area = heights[top] * width
            max_area = max(area,max_area)
        stack.append(i)
    return max_area



print(largest_rectangle([2, 1, 5, 6, 2, 3]))