def product_arr_expect_self(nums):
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [1] * n
    r_arr = [1] * n

    for i in range(n):
        j = -i-1
        l_arr[i] = l_mult
        r_arr[j] = r_mult

        l_mult *= nums[i]
        r_mult *= nums[j]
    return [ l*r for  l,r in zip(l_arr,r_arr)]





print(product_arr_expect_self([1,2,3,4]))
    