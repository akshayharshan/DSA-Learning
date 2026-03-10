arr = [1, 2, 3, 4, 6]
target = 6
l,r = 0, len(arr) - 1

while l < r:
    s = arr[l] + arr[r]
    if s == target:
        print(l,r)
        break
    if s > target:
        r -=1
    elif s < target:
        l +=1
