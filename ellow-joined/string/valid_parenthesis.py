def valid_parenthesis(s):
    hashmap = {')': '(', '}': '{', ']': '[' }
    result = []
    for char in s:
        if char not in '})]':
            result.append(char)
        else:
            if not result or result[-1] != hashmap[char]:
                return  False
            else:
                result.pop()
    return False if result else True





s = ")"
print(valid_parenthesis(s))
