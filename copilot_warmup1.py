"""
Q1: Given a string, return a dictionary of word → count.
Example: Input: "apple banana apple"
Output: { "apple": 2, "banana": 1 }
This tests:
splitting, iteration, hash maps, clarity of code
"""
from collections import defaultdict
str_to_split = "apple banana apple orange"
splitted = str_to_split.split(" ")
word_dict = {}
from collections import defaultdict, Counter
word_dict2 = defaultdict(int)
str_to_split = "apple banana apple orange"


def word_split(words_in:str):
    from collections import defaultdict
    w_dict = defaultdict(int) # only works on collections dict with auto‑initializes missing keys to 0, so += 1 is safe
    w_dict2 = {}
    for w in words_in.split():
        w_dict[w] += 1      # concise form if proper dict type obj initialized
        w_dict2[w] = w_dict2.get(w, 0) + 1   # default to 0 if key doesnt exist, else + 1

    return w_dict2

answer = word_split(str_to_split)

"""
Q2: Remove duplicates from a list while preserving order
Input: [3, 1, 3, 2, 1]  
Output: [3, 1, 2]

This tests:
sets   # a set is an unordered collection of unique values.
iteration, simple logic, incremental thinking
"""
in_list = [3, 1, 3, 2, 1]
s = set()
result = []

for i in in_list:
    if i in s:  # already exists
        continue
    else:       # new value add it
        s.add(i)
        result.append(i)

#print(s, result)
""" try above problem with dict taking advantage that keys are unique
🧭 Core idea: You maintain a single invariant:
    The ordered list always contains exactly the first occurrence of each value seen so far.
    
"""
in_list = [3, 1, 3, 2, 1]
def rmv_duplicates(num_list):       # BUT Fails to Preserve ORder as asked in orig question
    from collections import defaultdict, Counter
    num_count = defaultdict(int)
    for n in num_list:
        num_count[n] += 1

    unique_nums = [k for k, v in num_count.items() if v == 1]
    print(unique_nums)
    return unique_nums
uniq_nums = rmv_duplicates(in_list)
# Outer loop: runs n times and inner loop scans upto n elements for membership Performance is O(n sqrd2) ( n x n )
def keep_unique(num_list):    # simplest non set soln
    ordered = []
    for n in num_list:
        if n in ordered:    # we already saw number
            continue
        ordered.append(n)

    return ordered
uniq_nums_ordered = keep_unique(in_list)
# A dict is a hash table underneath, so checking membership doesn’t require scanning the accumulator.
#  Because dicts preserve insertion order, the keys reflect the first time each value appeared. This keeps the logic identical
#  to the list-based version but reduces membership checks from O(n) to O(1), making the whole algorithm linear.”
def unique_with_dicts(num_list):
    uniq_nums = {}

    for n in num_list:
        if uniq_nums.get(n):    # we already saw number
            continue
        uniq_nums[n] = True

    return list( uniq_nums.keys() )
uniq_nums_dict = unique_with_dicts(in_list)
"""
3. Find the first non‑repeating character
Input: "swiss"  
Output: "w"

This tests: counting, scanning, clean reasoning
"""
in_str = "swiss"
def find_non_repeat(word_str):
    from collections import defaultdict, Counter
    char_count = defaultdict(int)
    for n in word_str:
        char_count[n] += 1

    unique_chars = [k for k, v in char_count.items() if v == 1]  # list of non repeats
    # but now find the 1st occurrence non repeat letter
    for l in word_str:
        if l in set(unique_chars):   # want first occurrence of letter non repeat
            print("1st non-repeat letter :" , l)
            return(l)

first_letter = find_non_repeat(in_str)

def find_non_repeat2(word_str):
    # word_str gives you the correct chronological order
    # char_count gives you the global truth about repetition/freq occurrence
    from collections import defaultdict, Counter
    char_count = defaultdict(int)
    for n in word_str:
        char_count[n] += 1      # hash table of frequence
    # find all non‑repeats, then find the first one” into a single clean invariant:
    for l in word_str:  # walk the letters in correct order
        if char_count[l] == 1:      # use dict to exit quickly with answer, first letter freq == 1
            return l


not_rep = set()
repeats = set()
not_rep_list = []

len_str = len(in_str)
# loop thru each char in string
for i, char in enumerate(in_str):
    if (char not in not_rep) and (char not in repeats):
        not_rep.add(char)
        not_rep_list.append(char)
    else:   # char has appeared before drop it
        repeats.add(char)
        not_rep.discard(char)
        if char in not_rep_list:
            not_rep_list.remove(char)

print("first non repeating char is: ", not_rep_list[0], "entire not repeat list :", not_rep_list)

#  With basic Python only, this is the cleanest pattern:
def first_non_repeating_char(s):
    freq = {}

    # Count each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Find first character with count 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return None  # if all chars repeat


in_str = "swiss"
print("fastest basic py soln, freq counter" ,first_non_repeating_char(in_str))  # w

"""
What “O(n)” Really Means
O(n) means:

The work your algorithm does grows in direct proportion to the size of the input.

If the input doubles, the time roughly doubles.
If the input grows by 10×, the time grows by ~10×.

It’s linear growth.

Why O(n²) Happens — and Why Nested Loops Explode
The core idea
O(n²) means:

As the input grows, the work grows with the square of the input size.

If n doubles, the work becomes 4×.
If n triples, the work becomes 9×.

That’s why it “explodes.”

for i in items: 
    for j in items: 
        do_something(i, j)

if items has 1,000 elements:
Outer loop runs 1,000 times
Inner loop runs 1,000 times for each outer iteration

Total operations ≈ 1,000,000; That’s the explosion.
"""

"""
Warm‑Up Set #2 — Real‑world flavored (founder‑style)
[
  { user: "A", event: "login" },
  { user: "B", event: "click" },
  { user: "A", event: "logout" }
]

Output Expected:
{
  "A": ["login", "logout"],
  "B": ["click"]
}

"""
event_list = [
    { "user": "A", "event": "login" },
    { "user": "B", "event": "click" },
    { "user": "A", "event": "logout" }
]

user_dict = {}
# loop thru event list
for event in event_list:
#    print(event)
    keys = event.keys()
    user = event.get("user")
    u_event = event.get("event")
#    print(user, u_event)
    #
    if user_dict.get(user):
         user_dict[user].append(u_event)
    else:  # initialize key with new list
         user_dict[user] = [u_event]

#print(user_dict)

"""
5. Merge product updates: Given a list of product updates, keep only the latest update per product.
Input: [
  { id: 1, version: 1 },
  { id: 2, version: 1 },
  { id: 1, version: 2 }
]
Output: [
  { id: 1, version: 2 },
  { id: 2, version: 1 }
]
"""
updates = [ { "id": 1, "version": 1 }, { "id": 2, "version": 1 }, { "id": 3, "version": 1 }, { "id": 1, "version": 2 }, { "id": 2, "version": 2 } ]
updates = [
    {"id": 1, "version": 1},
    {"id": 1, "version": 2},  # duplicate of id=1, so output only has 1 entry after this
    {"id": 2, "version": 2},  # i=2 here, but output index for id=2 is actually 1
    {"id": 2, "version": 1},  # will try output[2] — IndexError or wrong slot
]
# use dict for output to match desired outcome of unique hash table updated thru loop
def prod_update(trans):
    product = {}
    for t in trans:
        id = t.get("id")
        ver = t.get("version")
        if id in product:    #product.get(id):  # we have this key, check version values to decide to update or not
            if product[id]["version"] < ver:    # we safely update whether data is sorted or not but avoids cost of sorting
                product[id] = t     #{"id": id, "version": ver}
        else:
            product[id] = t     # {"id": id, "version": ver}    # init with new id

    # product = {1: {'id': 1, 'version': 2}, 2: {'id': 2, 'version': 2}}
    return list(product.values())   # [{'id': 1, 'version': 2}, {'id': 2, 'version': 2}]

final_trans = prod_update(updates)


"""
When to use which pattern for py dict objs
Goal	                Best pattern
Check if a key exists	if key in dict:
Get a value safely	    value = dict.get(key)
Check existence and use the value	value = dict.get(key); if value is not None:
Avoid falsey-value traps	    Always use in or is not None
"""

user_index = {1: 0}
print(1 in user_index) # True
print(user_index.get(1)) # 0
print(bool(user_index.get(1))) # False <-- the trap

"""
6. Filter invalid records
Given a list of objects, return only those that have all required fields.
Input: data = [
    { "id": 1, "name": "A" },
    { "id": 2 },
    { "id": 3, "name": "C" }
]
output: [
  { id: 1, name: "A" },
  { id: 3, name: "C" }
]
"""
data = [ {"id": 1, "name": "A"}, {"id": 2}, {"id": 3, "name": "C"} ]
data = [
    {"id": 1, "name": "A"},
    {"id": 2, "extra_field": "oops"},  # invalid but contributes "extra_field" to valid_keys
    {"id": 3, "name": "C"}
]
required = {"id", "name"}

output3 = []
for r in data:
    # k in r on a dict checks if k is a key — so it's just saying "for every required key, is it in this dict?"
    # and all() makes sure every single one passes.  membership on a dict means key membership.
    # all([True, True, True])   # True  ;  all([True, False, True])  # False
    if all(k in r for k in required):
        output3.append(r)

print(output3)
# (k in r for k in required) produces something like [True, True]  # if both required keys are present
# [True, False]       # if one is missing

#simplest solution
required = {"id", "name"}
output2 = [r for r in data if required.issubset(r.keys())]
output3 = [r for r in data if all(k in r for k in required)]

print(output2, output3)

# helpful hints
required = {"id", "name"}        # this is a set
r.keys()                         # dict_keys(['id', 'name']) — set-like view
required.issubset(r.keys())      # "are all items in required present in r.keys()?"
required <= set(r.keys())        # <= on sets means "is subset of"

# Or the most readable alternative that doesn't require knowing issubset at all:
all(k in r for k in required)    # "for every required key, is it in the dict?"

"""
7. Flatten a nested list one level
Input: [1, [2, 3], 4, [5]]  
Output: [1, 2, 3, 4, 5]
Tests: loops, type checking, simple flattening
"""
input = [1, [2, 3], 4, [5]]
output = []

for d in input:
    if isinstance(d, list):
        output.extend(d)
        # output.extend([2, 3]) = output.append(2), # output.append(3)
        #for n in d:
        #    output.append(n)
    else:
        output.append(d)

print(output)

"""
Find the longest string in a list
Input: ["hi", "hello", "hey"]  
Output: "hello"
Tests: iteration,comparison, clarity
"""
data = ["hi", "hello", "hey"]
max_len = 0
long_string = ""

for d in data:
    if len(d) > max_len:
        max_len = len(d)
        long_string = d

lengths = [len(d) for d in data ]  # [2, 5, 3]
max_str = max(data, key=len)    # use a compare func in arg key=
print(long_string, max_str)

"""
ommon built-ins that take key=:
sorted(iterable, key=...)
min(iterable, key=...)
max(iterable, key=...)
Also list.sort(key=...) (method, not built-in function).
"""

# example 2
rows = [ {"id": 1, "version": 1}, {"id": 1, "version": 3}, {"id": 1, "version": 2}, ]
latest_row = max(rows, key=lambda r: r["version"])
print(latest_row)

scores = { "alice": 12, "bob": 7, "charlie": 19, "diana": 14 }
winner = max(scores.items(), key=lambda kv: kv[1])  # type(scores.items()) is a iterable yielding tuples
print(winner)

api_calls = {
    "GET /users": 1200,
    "POST /login": 450,
    "GET /orders": 980,
    "POST /checkout": 300
}
most_used = max(api_calls.items(), key=lambda kv: kv[1])
print(most_used)
"""
Mental model
max() → “Give me the item with the highest score.”
min() → “Give me the item with the lowest score.”
key= → “Here’s how to compute the score.”

Method	        Mutates original list	Returns a new list
list.sort()	    Yes	                    No (returns None)
sorted(iterable) No	                    Yes
"""

rows = [
    {"id": 1, "version": 3},
    {"id": 1, "version": 1},
    {"id": 1, "version": 2}
]
rows.sort(key=lambda r: r["version"])
sorted(rows, key=lambda r: r["version"], reverse=True)

print(rows)
rows.sort(key=lambda r: (r["id"], r["version"]))    # sort on multiple fields


scores = {"alice": 12, "bob": 7, "charlie": 19}
sorted_scores = sorted(scores.items(), key=lambda kv: kv[1])
print(sorted_scores)

"""
9. Reverse the words in a sentence
Input: "hello world from david"  
Output: "david from world hello"

Tests: splitting, reversing, joining
"""
data = "hello world from david"
words = data.split()     # ['hello', 'world', 'from', 'david']
output = []
last_word_idx = len(words)  # 4
for i in range(len(words)-1, -1, -1):
    print(i, words[i])
    output.append(words[i])

final_string = ""
final_string2 = ""
for w in output:
    final_string = final_string + " " + w
# fastest solution:  list(reversed(words))
for w in reversed(words):
    print(w)
final_string2 = " ".join(reversed(words))  # stitch back into a string
print(final_string2)

# word slice technique ; sequence[start : stop : step]
# If step is positive, default start=0, stop=len(seq)
# If step is negative, default start=len(seq)-1, stop=-1
# start at the end, # go until the beginning,  # step backwards by 1
# visualize what python does to fill in ==>  words[len(words)-1 : -1 : -1]
words[ : : -1]  # ['david', 'from', 'world', 'hello']
"hello"[::-1] # 'olleh'
final_string = " ".join(words[ : : -1])
"""  few more examples to cement the pattern

"""
words[::-2]     # => Reverse every other element:       ['david', 'world']
words[-2::-1]   # => Reverse but skip the last element: ['from', 'world', 'hello']
words[3:0:-1]   # => Reverse only the middle section:   ['david', 'from', 'world']

matrix = [
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32],
    [40, 41, 42]
]
""" Before:
Row 0 → [10, 11, 12]
Row 1 → [20, 21, 22]
Row 2 → [30, 31, 32]
Row 3 → [40, 41, 42]

Reverse the outer list (reverse the rows):  Python sees step = -1, so it defaults to: start at last row, walk backwards, stop before index -1
"""
matrix[::-1]
"""
After matrix[::-1]:
3: [40, 41, 42]
2: [30, 31, 32]
1: [20, 21, 22]
0: [10, 11, 12]

Reverse the inner lists (reverse each row)
"""

[row[::-1] for row in matrix]
"""
Row 0: [10, 11, 12] → [12, 11, 10]
Row 1: [20, 21, 22] → [22, 21, 20]
Row 2: [30, 31, 32] → [32, 31, 30]
Row 3: [40, 41, 42] → [42, 41, 40]

Reverse BOTH layers (full 180° flip)
"""
[row[::-1] for row in matrix[::-1]]
# [[42, 41, 40], [32, 31, 30], [22, 21, 20], [12, 11, 10]]




"""
10. Given a list of timestamps, group them into sessions
A session ends if more than 30 minutes pass between events.
input: [10:00, 10:10, 10:40, 11:20]
output: [ 
  [10:00, 10:10, 10:40],
  [11:20]
]
"""
# loop thru event times and keep track of previous time to check if 30min has passed
from datetime import datetime, time, timedelta
def add_minutes(t, minutes):
    if isinstance(t, datetime):
        t = t.time()
    return (datetime.combine(datetime.today(), t) + timedelta(minutes=minutes))

raw = ["10:00", "10:10", "10:40", "11:20"]
raw_times = [datetime.strptime(t, "%H:%M").time() for t in raw]

def time_to_datetime(t1):
    return datetime.combine(datetime.today(), t1)

times_list = [ time_to_datetime(t) for t in raw_times]
print("times_list converted to datetime",times_list)

output = [[] for _ in range(len(times_list))]

# set initial compare  start time
compare_time = times_list[0]
group = 0
for i, t in enumerate(times_list):
    print("datetime t:",t)
    if i == 0:
        output[group].append(t)
        continue
    else:
        compare_time = times_list[i-1]

    time_diff = (t - compare_time).total_seconds()
    print("time_diff secs: ",time_diff)
    if time_diff <= 1800:  # 30 min x 60s
        # add to current group
        output[group].append(t)
    else:
        # increment group and reset start time
        group +=1
        compare_time = times_list[i - 1]
        output[group].append(t)

print(output)

# Q10 better more elegant solution
from datetime import datetime, timedelta
raw = ["10:00", "10:10", "10:40", "11:20"]
times = [datetime.strptime(t, "%H:%M") for t in raw]
sessions = []
# init first group in output
current = [times[0]]

# zip to compare consecutive pairs — very Pythonic; zip(a, b) stops when the shorter list ends
# zip(times, times[1:]) produces 3 pairs: (10:00, 10:10) (10:10, 10:40) (10:40, 11:20)
for prev, curr in zip(times, times[1:]):
    if curr - prev <= timedelta(minutes=30):
        current.append(curr)
    else:
        sessions.append(current)
        current = [curr]
# loop ends with current = 11:20  last value
sessions.append(current)

print(sessions)

# Q10 functionlize soln
from datetime import datetime, timedelta

def group_sessions(raw_times, gap=30):
    times = [datetime.strptime(t, "%H:%M") for t in raw_times]
    sessions = []
    current = [times[0]]

    for prev, curr in zip(times, times[1:]):
        if curr - prev <= timedelta(minutes=gap):
            current.append(curr)
        else:
            sessions.append(current)
            current = [curr]

    sessions.append(current)    # account for last loop
    return sessions

print(group_sessions(["10:00", "10:10", "10:40", "11:20"]))
