def merge_sorted_array(arr1,arr2):
    result = []
    left_arr  = len(arr1)
    right_arr =  len(arr2)
    l = 0
    r = 0
    while l < left_arr and r  < right_arr:
        if arr1[l] <= arr2[r]:
            result.append(arr1[l])
            l += 1
        else:
            result.append(arr2[r])
            r +=1
    result = result + arr1[l:]
    result = result + arr2[r:]
    return result
    
    









arr1 = [1,3,5]
arr2 = [2,4,6]

print(merge_sorted_array(arr1,arr2))