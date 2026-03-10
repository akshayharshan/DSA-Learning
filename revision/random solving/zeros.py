# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

arr = [0,1,0,3,12]
l=0 

for r in range(len(arr)):
    if arr[r] != 0:
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
print(arr)

        
