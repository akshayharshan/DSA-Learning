def maximum_swap(arr):
    n = len(arr)
    max_indx = [0] * n
    max_pos = 0

    for i in range(n-1,-1,-1):
        if arr[i] > arr[max_pos]:
            max_pos = i
        max_indx[i] = max_pos

    for i in range(len(arr)):
        if arr[max_indx[i]] > arr[i]:
            arr[i],arr[max_indx[i]] = arr[max_indx[i]],arr[i]
    return arr



nums = [1,3,2,7]
print(maximum_swap(nums))