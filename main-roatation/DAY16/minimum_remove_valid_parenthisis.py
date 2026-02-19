def min_remove_valid_parentheses(string):
    stack=[]
    invalid_set = set()

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        if string[i] ==  ')':
            if not stack:
                invalid_set.add(i)
            else:
                stack.pop()

    invalid_set.update(stack)
    chars = list(string)
    new_string = []
    for i in range(len(string)):
        if i not in invalid_set:
            new_string.append(string[i])
    new_string = "".join(new_string)


    return new_string
             


string = "lee(t(c)o)de)"

print(min_remove_valid_parentheses(string))