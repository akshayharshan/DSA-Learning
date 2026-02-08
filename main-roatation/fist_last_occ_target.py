
# def first_last_occur(nums,target):
#     l,r = 0 , len(nums)-1
#     left = -1
#     right = -1
#     while l<=r:
#         if nums[l] == target and left == -1:
#             left = l
#         if nums[r] == target and right == -1:
#             right = r
#         if right != - 1 and left != -1:
#             break
#         l+=1
#         r-=1
        
#     return [left,right]




# nums = [1, 2, 2, 2, 3, 4]
# target = 2
# print(first_last_occur(nums,target))









def first_last_occur(nums,target):
    l,r = 0 , len(nums)-1
    first = -1
    last = -1
    while l<=r:
        mid = l + (r-l)//2

        if nums[mid] == target:
                first = mid
                r = mid - 1
        
        elif(nums[mid] > target):
            r = mid - 1
        else:
            l = mid + 1

    l =0
    r=len(nums)-1

    while l<=r:
        mid = l + (r-l)//2

        if nums[mid] == target:
                last = mid
                l = mid + 1
        
        elif(nums[mid] > target):
            r = mid - 1
        else:
            l = mid + 1
            
    return [first,last]








nums = [1, 2, 2, 2, 3, 4]
target = 2
print(first_last_occur(nums,target))

