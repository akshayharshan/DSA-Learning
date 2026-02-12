def majority_element(nums):
    candidate=None
    count=0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count+=1
        else:
            count-=1
    print(candidate,count)


    return candidate if count > 0 else None


nums = [2,2,1,1,1,2,2]
print(majority_element(nums))