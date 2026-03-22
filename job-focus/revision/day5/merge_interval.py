def merge_interval(intervals):
    intervals = sorted(intervals)
    res = []
    period = intervals[0]

    for i in range(1,len(intervals)):
        if intervals[i][0] <= period[1]:
            period[1] = max(period[1],intervals[i][1])
        else:
            
            res.append(period)
            period = intervals[i]

    res.append(period)
    return res


intervals = [[1,3],[2,4],[3,5]]
print(merge_interval(intervals))