def duplicate(nums):
    hashmap = set()
    result = []
    for num in nums:
        if num not in hashmap:
            hashmap.add(num)
            result.append(num)
    return result






nums = [5, 5, 5, 5]

print(duplicate(nums))