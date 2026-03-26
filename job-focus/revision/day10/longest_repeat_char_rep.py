def longest_repeat_char(s,k):
    l = 0
    counts = [0] * 26
    longest = 0
    for r in range(len(s)):
        counts[ord(s[r]) - 65] += 1
        while (r - l) + 1 - counts[ord(s[r]) - 65] > k:
            counts[ord(s[l]) - 65] -= 1
            l+=1
        longest = max(r-l+1,longest)
    return longest

             



s = "AABABBA"
k = 1
print(longest_repeat_char(s,k))