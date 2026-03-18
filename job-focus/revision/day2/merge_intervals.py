def merge_intervals(intervals):
    intervals = sorted(intervals)
    res = []
    if len(intervals) < 2 :
        return intervals
    curr_inter = intervals[0]
    for inter in range(1,len(intervals)):
        if curr_inter[1] >= intervals[inter][0]:
            curr_inter[1] = max(curr_inter[1],intervals[inter][1])
        else:
            res.append(curr_inter)
            curr_inter = intervals[inter]
    res.append(curr_inter)
    return res 




test_cases = [
    # [[1, 3], [2, 6], [8, 10], [15, 18]],
    # [[1, 4], [2, 3]],
    [[1, 2], [3, 4], [5, 6]],
    # [[1, 4], [4, 5]],
    # [[8, 10], [1, 3], [2, 6]],
    # [[1, 5]],
    []
]

for case in test_cases:
    print("Input:", case)
    print("Output:", merge_intervals(case))
    print("-" * 30)