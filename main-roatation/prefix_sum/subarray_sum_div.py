def prefix_sum(nums,k): 

  prefix_sum = 0
  seen = set()
  seen.add(0)

  for num in nums:
        prefix_sum +=num
        reminder = prefix_sum % k
        if reminder in seen:
            return True
        seen.add(reminder)
  return False






nums = [1, 2, 3]
k = 7
print(prefix_sum(nums,k))


