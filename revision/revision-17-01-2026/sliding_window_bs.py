# Option A — Sliding Window

# Mentally re-explain:

# expand vs shrink

# window size = r - l + 1

# Option B — Binary Search

# Write classic binary search once (no pressure)

# Just to keep it alive


# expand is used here for finding the varying sliding window to find the lenth of longest substring while going through the string we had kept the element
# we saw in the  array if one element saw more than once remove it from the seen array list and also update the max_len we cant took the len of seen but we will take r-l+1

# the r and l start at 0 and r move as we found the unique element if a element is already seen then move the left pointer


arr = [1,2,3,4,18,24]
l =0
r = len(arr) - 1
target = 18

while l <=r:
    mid = l+(r-l)//2
    if arr[mid] == target:
        print(mid)
        break
    if arr[mid] > target:
        r = mid - 1
    else:
        l = mid + 1


