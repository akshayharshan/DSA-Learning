def min_remove_valid_parentheses(string):
    remove_list = []
    stack = []

    for i in range(len(string)):

        if string[i] == '(':
            stack.append(i)
        if string[i] == ')':
            if not stack:
                remove_list.append(i)
            else:
                stack.pop()
    if stack:
        remove_list.extend(stack)

    new_str = ''

    for i in range(len(string)):
        if i not in remove_list:
            new_str += string[i]
    return new_str
        

string = "lee(t(c)o)de)"
print(min_remove_valid_parentheses(string))