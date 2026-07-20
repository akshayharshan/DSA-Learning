
def duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return False
        seen.add(num)
    return True


nums = [1,2,3,1]
print(duplicate(nums))