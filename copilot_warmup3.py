"""  Compute rolling averages
Given a list of numbers and a window size k, compute the rolling average.
Real question:   What happens when the window doesn’t fit?
Do we use integer or float division?
Skills trained: sliding windows; boundary conditions; incremental computation
input: nums = [10, 20, 30, 40];  k = 2
output: rolling_avg = [15, 25, 35]

Observed : output list will always be 1 smaller than input list since once at last number, stop avg compute
Idea? only start computing avg on index 1 forward;
    keep track of previous number value thru iterate;
    sp on idx=1; total = previous + current => (10 + 20) / k=2 ==> 15
"""

nums = [10, 20, 30, 40]
k = 2
# wanted output rolling_avg = [15, 25, 35]

output = []
for i in range(0, len(nums)):
    print(i)
    if i > 0:  # then compute
        total = nums[i] + nums[i-1]
        roll_avg = total / k
        output.append(roll_avg)

print(output)

# now try with k=3 must get 3 numbers to avg
output = []
k=3
for i in range(0, len(nums)):
    window = nums[max(0, i - 2): i + 1]
    print(window, sum(window))
    if i > 1:  # then compute
        roll_avg = sum(window) / k
        output.append(roll_avg)

print("rolling avgs: ", output)

# generalized func for any K value
def rolling_avg(nums_list: list, k:int):
    avg_list = []
    window_range = (k-1)

    # if i >= (k-1):  # then compute as only then do we have enough values to total
    for i in range(window_range, len(nums_list)):
        # slice list properly as we dont want negative values
        window = nums[max(0, i - window_range): i + 1]
        print(window, sum(window))
        roll_avg = sum(window) / k
        avg_list.append(roll_avg)

    return avg_list

nums = [10, 20, 30, 40, 50, 60]
output = []
output = rolling_avg(nums_list=nums, k=4)
print("rolling avgs: ", output)

# most efficient version think of the window as starting at index i:
# This perspective is common in algorithmic interviews because it aligns with “iterate forward and take the next k items.”
i = 0
nums = [10, 20, 30, 40, 50]
window = nums[i : i+k]

def rolling_avg_best(nums, k):
    out = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        out.append(sum(window) / k)
    return out

output = []
output = rolling_avg_best(nums, k=4)
print("rolling avgs: ", output)
