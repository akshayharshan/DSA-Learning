def balanced_parentheses(string):

    stack = []
    str_list = list(string)
    hashmap = {'}' : '{' , ')' : '(' , ']' : '['}
    for i in range(len(str_list)):
        if str_list[i] in '{([':
            stack.append(str_list[i])
        else:
            if stack and stack[-1] == hashmap[str_list[i]]:
                stack.pop()
            else:
                return False
                
    return True if not stack else False






print(balanced_parentheses("(]"))