def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    # At a point the recusrsion will stop when it reach the dividing and to the end like if array is [1,2,3]
    # it will divide till it reach [1] then contiue the sorting mechanism so first give left side and right array side 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

#Here the left pointer sorting happens the left pointer focus on the left side array and right pointer focus on right array
# at a point the right or left will out bound the while condition so the remaining left overs where pushed to the sorted array using extend and array slicing method
def merge(left,right):
    l,r=0,0
    sorted_array = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_array.append(left[l])
            l+=1 
        else:
            sorted_array.append(right[r])
            r+=1
    sorted_array.extend(left[l:])
    sorted_array.extend(right[r:])
    return sorted_array


print(merge_sort([1,0,-1,52,3,4,7,11,90,32,14,46]))