def sub_array_sum(nums,k):

    hashmap = {0:1}
    count = 0
    prefix_sum = 0

    for num in nums:
        prefix_sum+=num
        prev_sum = prefix_sum -k
        if prev_sum in hashmap:
            count += hashmap[prev_sum]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1
    return count
print(sub_array_sum([1,2,3,4,5,20],3))




def longest_substring(s):
    max_len = 0
    l = 0
    hashmap = set()

    for r in range(len(s)):
        
        while s[r] in hashmap:
            hashmap.remove(s[l])
            l+=1
        hashmap.add(s[r])
        max_len = max(max_len,r-l +1)
    return max_len





print(longest_substring("abcabcbb"))