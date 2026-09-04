def sort_num(nums):
    counts = [0,0,0]

    for color in nums:
        counts[color] += 1
    
    R,W,B = counts

    nums[:R] = [0] * R
    nums[R:R+W] = [1] * W
    nums[R+W:] = [2] * B
    return nums




print(sort_num([2,1,0,1,2,0]))