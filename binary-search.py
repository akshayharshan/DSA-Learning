arr = [1,4,5,6,7,8,9]
target = 8
n = len(arr)
l,r=0,n-1

while l <= r:
    mid = r-l//2
    if target == arr[mid]:
        print(mid)
        break
    if arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

