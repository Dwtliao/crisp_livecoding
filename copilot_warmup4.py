"""
Build a tiny search index
data = [   "apple banana",
  "banana carrot",
  "apple carrot" ]

indexed_results = {
  "apple": [0, 2],
  "banana": [0, 1],
  "carrot": [1, 2]
}
Asssumptions: for each word encountered, take note of position, record in a dict hash lookup;
when new work initialize it; when re-encountered, simply update dict key's value
"""

data = [
  "apple banana",
  "banana carrot",
  "apple carrot"
]
# words[0].split() = ['apple', 'banana']

def index_words(word_list):

    word_idx = {}
    # idea: loop thr words of each row split and just take note of positions?
    for idx, r in enumerate(word_list):
        keys = r.split()
        print(f"row {idx}: has ", " ,".join(keys))

        for k in set(r.split()):    # set to avoid counting duplicate words in same row
            # word_idx[k] = [].append(idx)
            word_idx.setdefault(k, []).append(idx)

    return word_idx

results = index_words(data)
print(results)


"""
Warm-up Problem: Longest Increasing Run
Given a list of integers, return the length of the longest strictly increasing contiguous run.
Example:
[1, 2, 2, 3, 4, 1] → longest increasing run is [2, 3, 4] → return 3

Assumptions:  keep track of current streak and reset when a new streak starts but save prev streak for comparision
"""
numbers = [1, 2, 2, 3, 4, 1, 2, 3, 4, 5]

def longest_run(nums_list):
    # initialize states, keep integers of best streak?
    last = nums_list[0]
    current_streak = [last]
    best_streak = []

    for n in nums_list[1:]:     #skip 1st row
        if n > last:            # continue streak if continuous
            current_streak.append(n)
        else:                   # current streak ended
            if len(best_streak) < len(current_streak):
                best_streak = current_streak
            current_streak = [n]    # reset with starting number
        last = n                    # always update last at end of Loop

    # check last streak against best streak before exit
    if len(best_streak) < len(current_streak):
        best_streak = current_streak

    return len(best_streak), best_streak

longest, streak = longest_run(numbers)
print(longest, streak)


