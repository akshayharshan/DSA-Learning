def dutchFlag(arr):
    slow = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            arr[slow],arr[i] = arr[i],arr[slow]
            slow+=1
    for i in range(len(arr)):

        if arr[i] == 1:
            arr[slow],arr[i] = arr[i],arr[slow]
            slow+=1
    return arr


arr = [2,0,1]
print(dutchFlag(arr))