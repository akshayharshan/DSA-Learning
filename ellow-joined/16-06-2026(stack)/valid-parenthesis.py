def validParenthesis(strs):
    stack = []
    hashmap = {'}':'{', ')' : '(' , ']' : '['}

    for char in strs:
        if char in '{([':
            stack.append(char)
        else:
            if not stack:
                return False
            elif not hashmap.get(char) or stack[-1] != hashmap.get(char):
                return False
            stack.pop()
    return False if stack else True


s = "()[]{}"
print(validParenthesis(s))
