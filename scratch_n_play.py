input = [(1, 3), (2, 4), (6, 8), (7, 9)]
input2 = [(2, 4), (1, 3), (6, 8), (7, 9)]

def check_overlap(a:tuple, b:tuple):
    # a and b are tuples with (start, end); of b(start) <= a(end) value then overlap is True
    if b[0] <= a[1]:
        return True
    return False

def merge_tuple(a:tuple, b:tuple):
    # a and b are tuples with (start, end); Why max is required: the three possible shapes of overlap
    # A ends later than B => A = (1, 10) ; B = (2, 4) merged wanted is (1, 10)
    #  the merged interval’s end must be the furthest right endpoint.
    return (a[0], max(a[1], b[1]) )


sorted_in = sorted(input)
merged = []
curr_tuple = sorted_in[0]

for curr, next in zip(sorted_in, sorted_in[1:]):
    print("curr: ", curr, "next:",next)
    if check_overlap(curr, next):
        curr_tuple = merge_tuple(curr, next)
    else:
        # append to final output current
        merged.append(curr_tuple)
        curr_tuple = next

# final output append last tuyple
merged.append(curr_tuple)
print(merged)

""" Alternate CoPilot solution """


def merge_intervals(intervals):
    intervals = sorted(intervals)  # sort by start
    merged = []

    for interval in intervals:
        if not merged:  # 1st loop init merged with 1st tuple to start, continue to next iteration
            merged.append(interval)
            continue

        last = merged[-1]
        if interval[0] <= last[1]:  # overlap condition update current merged tuple with max value
            merged[-1] = (last[0], max(last[1], interval[1]))
        else:
            merged.append(interval)

    return merged
