
# revision on 04/06/2026

def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])
    result =  [intervals[0]]

    for curr in intervals[1:]:
        last = result[-1]
        
        if curr[0] <= last[1]:
            last[1] = max(curr[1],last[1])
        else:
            result.append(curr)
    return result









intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))

