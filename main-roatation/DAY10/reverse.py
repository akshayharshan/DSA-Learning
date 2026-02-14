def reverse_array(nums):
    # using range method
    # rev_arr = []
    # for i in range(len(nums)-1,-1,-1):
    #     rev_arr.append(nums[i])
    # return rev_arr
    
    
    #uisng two pointer

    l,r= 0,len(nums) - 1
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    return nums






nums = [1,2,3,4,5]
print(reverse_array(nums))