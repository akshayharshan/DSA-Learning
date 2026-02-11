def prefix_sum(nums): 

  prefix_sum = 0
  seen = set()
  seen.add(0)

  for num in nums:
        prefix_sum +=sum
        if prefix_sum in seen:
            return True
        seen.add(prefix_sum)
  return False






nums = [4, 2, -3, 1, 6]
k = 3
print(prefix_sum(nums,k))