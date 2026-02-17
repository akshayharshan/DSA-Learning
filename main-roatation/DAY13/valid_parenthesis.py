def valid_parenthesis(string):
    stack = []
    hashmap = {'}': '{' , ']': '[' , ')':'('}
    for char in string:
        if char not in "})]":
            stack.append(char)
        elif not stack or stack[-1] != hashmap[char]:
            return False
        else:
            stack.pop()
    return True if not stack else False 






string = "{[]}"
print(valid_parenthesis(string))