def merge_intervel(intervels):
    result = []
    n = len(intervels)
    intervel = 0

    while intervel < n:
        if intervels[intervel + 1][0] <= intervels[intervel][1]:
            result.append([intervels[intervel][0],intervels[intervel+1][1]])
            intervel +=2
        else:
            result.append(intervels[intervel])
        intervel+=1
    return result 
    




print(merge_intervel([[1,3],[2,6],[8,10],[15,18]]))