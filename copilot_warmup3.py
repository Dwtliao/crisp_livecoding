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
i = 0   # k=4 then i values are: 0, 1.
nums = [10, 20, 30, 40, 50]
# visualize you need k numbers to compute rolling avg so range to iterate is i: i+k
k=4
window = nums[i : i+k]

def rolling_avg_best(nums, k):
    out = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        out.append(sum(window) / k)
    return out

output = rolling_avg_best(nums, k=4)    # i values are: 0, 1.
print("rolling avgs: ", output)         # [25.0, 35.0]


"""
Detect anomalies in a sequence
Given a list of integers, return all values that are more than 2 standard deviations from the mean..

Real question:  Do we compute mean and std once or update dynamically?
What about empty lists?
Skills trained: statistical reasoning ; edge cases ; defining thresholds

let's start with math formulas required for Std Deviation

mean = sum(values) / k  (k = len(values or numbers in a list) )

variance = sum((x - mean) ** 2 for x in values) / k
Std Deviation = SquareRoot(variance)
"""
# create math functions we need
import math


def mean(n: list):
    k = len(n)
    return float(sum(n) / k)

def std_dev(values):
    k = len(values)
    mean = sum(values) / k
    variance = sum( (x - mean) ** 2 for x in values ) / k
    return math.sqrt(variance)

def two_std_from_mean_left(sdv, mean):
    return (mean - (2 * sdv))

def two_std_from_mean_right(sdv, mean):
    return (mean + (2 * sdv))


num_values = list(range(1,20))
print(num_values)
num_stddev = std_dev(num_values)
num_mean = mean(num_values)
print("std dev ", num_stddev, "mean ", num_mean)
# 2 std deviations from mean
compare_value_left = two_std_from_mean_left(num_stddev, num_mean)
compare_value_right = two_std_from_mean_right(num_stddev, num_mean)
print("compare_values are [ ", compare_value_left, "to" , compare_value_right, "]")

keep2 = [n for n in num_values if n < compare_value_left or n > compare_value_right]

keep = []
for n in num_values:
    if n < compare_value_left or n > compare_value_right:   #
        keep.append(n)
        print("keep ", n)

# A simple, interview‑ready version of the code
def anomalies(nums):
    if not nums:
        return []

    mean = sum(nums) / len(nums)
    variance = sum((x - mean)**2 for x in nums) / len(nums)
    std = variance ** 0.5

    lower = mean - 2*std
    upper = mean + 2*std

    return [x for x in nums if x < lower or x > upper]
"""
The invariant is: center = mean ; radius = std  ; threshold = 2 × radius ; compare distance to threshold
This is the same structural reasoning you used in the timestamp session problem: define the boundary, then filter.
"""

"""
Deduplicate customer records:  What defines a duplicate?  ID? Email? Both?  Which record wins if fields differ?
Skills trained: clarifying requirements ; defining equality ; choosing data structures
[ {"id": 1, "email": "a@example.com"},
  {"id": 2, "email": "b@example.com"} ]

"""

data = [
    {"id": 1, "email": "a@example.com"},
    {"id": 1, "email": "a@example.com"},
    {"id": 2, "email": "b@example.com"},
    {"id": 2, "email": "b2@example.com"}
]
# assumptions: each row is a dict where id and email are both keys to check for dups
# assumptions: same id value can have multiple diff emails and those are 2 different customer records
def rmv_duplicates(cust_recs):
    unique = []

    for r in cust_recs:
        id = r["id"]
        email = r["email"]
        if r in unique:
            continue
        # else this is a new unique row
        unique.append(r)

    return(unique)

no_dups = rmv_duplicates(data)

# SAFER approach built a tuple of value pairs for comparison in a set which enforcees uniqueness
def rmv_duplicates_sig(records):
    seen = set()
    unique = []

    for r in records:
        sig = (r["id"], r["email"])   # the fields that define uniqueness
        if sig in seen:
            continue
        seen.add(sig)
        unique.append(r)

    return unique

# Safest approach If rows might contain the same data but in different shapes (extra fields, different ordering), you can normalize them.
def rmv_duplicates_normalized(records):
    seen = set()
    unique = []
    """ Rows may have inconsistent key ordering.  Rows may have extra fields.  You want to compare entire dict content.
    """

    for r in records:
        normalized = tuple(sorted(r.items()))   # Normalization is a “defensive programming” move.
        if normalized in seen:
            continue
        seen.add(normalized)
        unique.append(r)

    return unique

# You’re not relying on Python’s dict equality semantics.
def rmv_duplicates_define_uniq(records):
    unique = []
    for r in records:
        if not any(r["id"] == u["id"] and r["email"] == u["email"] for u in unique):
            unique.append(r)
    return unique

""" 
switch the uniqueness rule from (id, email) to email only, the entire shape of the problem changes. 
a deeper, more ambiguous question: If multiple IDs share the same email, what does that mean, and which record should survive?
"""
# assumptions : intent is to Merge multiple ID(s) for same email so data info is preserved not lost

emails = [
    {"id": 1, "email": "a@example.com"},
    {"id": 3, "email": "a@example.com"},
    {"id": 2, "email": "b@example.com"},
    {"id": 4, "email": "b2@example.com"},
    {"id": 3, "email": "a@example.com"},
]

def merge_email_ids(data):
    #from collections import defaultdict
    #unique = defaultdict(list)
    unique = {}
    for d in data:
        if d["email"] in unique:
            unique[d["email"]].append(d["id"])  # add to existin list of ids
        else:
            unique[d["email"]] = [d["id"]]      # init with first id

    return unique

emails_uniq = merge_email_ids(emails)
emails_uniq_list = [{"email": email, "ids": ids} for email, ids in emails_uniq.items()]

def merge_email_ids2(data):
    unique = {}
    for d in data:
        email = d["email"]
        unique.setdefault(email, []).append(d["id"])    # setdefault to avoid explicit if/else, but logic is identical.
    return unique


def merge_email_ids_sets(data):
    unique = {}
    for d in data:
        email = d["email"]
        id_ = d["id"]
        if email in unique:
            unique[email].add(id_)
        else:
            unique[email] = {id_}   # correct single-item set

    return [{"email": email, "ids": list(ids)} for email, ids in unique.items()]

emails_uniq_set = merge_email_ids_sets(emails)

"""
Reconstruct a message from fragments: Is order guaranteed?? Should we trim whitespace?  What if fragments overlap?
frag = ["Hel", "lo ", "Wor", "ld"]
msg = "Hello World"

Assumptions: if there is a white space at end of a string assume the previous word has ended
"""
frag = ["Hel", "lo ", "Wor", "ld,", "go", "od ", "morning"]


def reconstruct1(f_list):
    words = []
    current = ""
    # what is condition to start a new word?
    for idx, f in enumerate(f_list):
        if (" " in f) or (',' in f) or (idx+1 == len(f_list)):  # assume current word is ending or end of list of fragments
            current = current + "".join(f)
            words.append(current)
            current = ""
        else:
            current = current + "".join(f)

    return " ".join(words)

final_msg = reconstruct1(frag)
print(final_msg)

# assume current word is ending or end of list of fragments;  You didn’t need to know you were on index 3.
# You only needed to know: # “current ends with a boundary?”
# “is current non‑empty after the loop?”  # That’s the invariant.
def reconstruct2(f_list):
    words = []
    current = ""
    for f in f_list:
        current += f
        if current.endswith((" ", ",")):    # endswith() matches the semantic boundary, not the fragment boundary.
            words.append(current.strip())
            current = ""

    if current:     # append final fragment
        words.append(current)

    return " ".join(words)

final_msg = reconstruct2(frag)
print(final_msg)

""" Grouping: flush when the key changes ; Group sorted rows by user_id.
"""
def group_rows(rows):
    groups = []
    current_user = None
    current_rows = []

    for row in rows:
        if row["user_id"] != current_user:
            if current_rows:
                groups.append(current_rows)
            current_user = row["user_id"]
            current_rows = []
        current_rows.append(row)

    if current_rows:
        groups.append(current_rows)

# Split a string into tokens without using .split().
def split_string_on_space(text):
    tokens = []
    current = ""

    for ch in text: #traverse each char in long string
        if ch.isspace():
            # If there are multiple spaces, you’d keep hitting whitespace again.
            if current:
                tokens.append(current)  #
                current = ""
        else:
            current += ch

    if current:
        tokens.append(current)
    return tokens

test_split =  split_string_on_space("this is a    long string.")
print(test_split)


"""  Find the longest streak of consecutive days
days = ["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05", "2024-01-06"]
result = ["2024-01-04", "2024-01-06"]

assumptions: sort the given list first so we can work with sorted list as iteration 1
keep track of len of current range and overwrite after a new winner is found
"""
days = ["2024-01-01", "2024-01-02", "2024-01-04", "2024-01-05", "2024-01-06"]


def find_consec_days(strings):
    from datetime import datetime
    dates = [datetime.strptime(s, "%Y-%m-%d").date() for s in strings]
    start = None
    prev = None
    prev_streak_len = 0
    current_len = 0     # len of current consecutive streak
    # expect date delta to be 1 day apart, if not save current streak and start counting next streak

    for d in sorted(dates):
        if start is None:   # 1st loop pass
            start = d
            delta = 0
        else:
            delta = (d - prev).days     # what is current date diff to prev date

        if delta > 1:               # reset start date
            if current_len > prev_streak_len:
                current_streak = [start, prev]
                prev_streak_len = current_len

            start = d
            prev = d
            current_len = 0
            continue

        # delta = 1 or 0, keep current streak alive
        prev = d
        if delta == 1:       # only increment if delta is one day, skips loop 1
            current_len += 1


    # loop has ended check current streak
    if current_len > prev_streak_len:
        current_streak = [start, prev]
    # we have a tie?  keep both streaks
    elif current_len == prev_streak_len:
        if current_streak:
            current_streak.append([start, prev])

    return current_streak

longest_streak = find_consec_days(days)
longest_streak

# simpler cleaner version using slice
def find_consec_days_slice(strings):
    from datetime import datetime
    dates = sorted(datetime.strptime(s, "%Y-%m-%d").date() for s in strings)

    best_start = best_end = None
    best_len = 0

    curr_start = curr_end = dates[0]
    curr_len = 0

    for d in dates[1:]:
        if (d - curr_end).days == 1:
            curr_end = d
            curr_len += 1
        else:
            if curr_len > best_len:
                best_len = curr_len
                best_start, best_end = curr_start, curr_end
            curr_start = curr_end = d
            curr_len = 0

    if curr_len > best_len:
        best_start, best_end = curr_start, curr_end

    return [best_start, best_end]
