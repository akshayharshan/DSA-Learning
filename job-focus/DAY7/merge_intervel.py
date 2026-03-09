def merge_intervel(intervals):
    intervals = sorted(intervals)
    result =[]

    curr = intervals[0]
    for i in range(1,len(intervals)):

        if   intervals[i][0] <= curr[1]:
            curr[1] = max(curr[1],intervals[i][1])
        else:
            result.append(curr) 
            curr = intervals[i]
    result.append(curr)    
    return result






print(merge_intervel([[1,6],[2,4],[7,9]]))