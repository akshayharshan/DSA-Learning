def balanced_bracket(string):
    stack = []

    hashmap = {'}' : '{' , ')' : '(', ']' : '['}

    for char in string:
        if char in  '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] != hashmap[char]:
                return False
            stack.pop()
    return len(stack) == 0







string = "]"
print(balanced_bracket(string))