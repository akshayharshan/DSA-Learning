def daily_temp(temps):

    stack = []
    result= [0] * len(temps)

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            index = stack.pop()
            result[index] =  i - index
        stack.append(i)
    return result







temps = [73,74,75,71,69,72,76,73]
print(daily_temp(temps))