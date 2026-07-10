def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False


nums = [1,2,3,1]
print(contains_duplicate(nums))

