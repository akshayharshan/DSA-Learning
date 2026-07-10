# Example Test Case
def find_pairs_with_difference(nums,target):
    seen = set(nums)
    result = set()

    for num in nums:
        diff =  num - target
        if diff in seen:
            result.add((num,diff))

    return result





numbers = [1, 5, 3, 4, 2, 2, 3]
target = 2
result = find_pairs_with_difference(numbers, target)

print(result)