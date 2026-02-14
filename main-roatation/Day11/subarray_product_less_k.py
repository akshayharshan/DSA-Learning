def subarray_product(nums,k):

    product = 1
    count = 0
    l = 0

    if k <=1:
        return 0
    for r in range(len(nums)):
        product *= nums[r]

        while product >= k:
            product /= nums[l]
            l+=1
        count += r-l+1
    return count



nums = [10, 5, 2, 6]
k = 100
print(subarray_product(nums,k))