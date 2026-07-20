def two_string_permutation(s1,s2):
    window_size = len(s1) 
    s1_freq = {}
    window_freq = {}
    for i in range(len(s1)):
        s1_freq[s1[i]] = s1_freq.get(s1[i],0) + 1
    l = 0
    for r in range(len(s2)):
        window_freq[s2[r]] = window_freq.get(s2[r],0) + 1
        size = r-l+1
        if size > window_size:
            window_freq[s2[l]] = window_freq.get(s2[l],0) - 1
            if window_freq[s2[l]] < 1 :
                window_freq.pop(s2[l])
            l += 1
        if window_freq == s1_freq:
            return True
    return False






s1 = "ab"
s2 = "eidbaooo"

print(two_string_permutation(s1,s2))
