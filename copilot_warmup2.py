"""
“What is this problem really asking?”
1. Normalize product SKUs
You receive a list of product SKUs that may contain inconsistent formatting:
["abc-123", "ABC123", "abc_123", "Abc-123 "]

Return a list of normalized SKUs where:
letters are uppercase;  separators are removed;  whitespace is trimmed

Real question:
Can you identify the canonical representation before coding?
Skills trained:
clarifying assumptions,  defining invariants,  designing helper functions
"""
skus = ["abc-123", "ABC123", "abc_123", "Abc-123 "]

# assumptions, looks like SKU pattern is x letters and x numbers and possible separators which can be multiple things
# like even white space but expect to have to remove some kind of separator

"""
A founder‑level assumption sounds like this:
“The only reliable signal is alphanumeric characters.
Anything that is not a letter or digit is noise.
The canonical form is uppercase letters + digits with no separators or whitespace.”
This avoids assuming: order, length, grouping, meaning of separators, presence of separators
It also aligns perfectly with the prompt’s real question:
Can you identify the canonical representation before coding?

The clearest single‑sentence statement of the canonical pattern is:
“A normalized SKU is the uppercase sequence of all alphanumeric characters in order, with all whitespace and separators removed.”
This is the version that sounds senior and calm:

“I’ll write a small helper that takes a character, uppercases it, and returns it only if it’s’ll write a small helper that takes a character, uppercases it, and returns it only if it’s a letter or digit. I can check that either with Python’s isalnum() or like A–Z and 0– by comparing ranges9. The key is that only alphanumeric characters survive.”
"""
skus = ["abc-123", "ABC123", "abc_123", "Abc-123 "]

def check_alphanumeric(c: str):
    # expect string to be passed
    C = c.upper()
    if ("A" <= C <= "Z") or ("0" <= C <= "9"):
        return C
    return None

def check_isalnum(c: str):
    # yes if char is alpha char or numbers
    if c.isalnum():
        return c.upper()
    else:
        return None

cleaned_skus = []
for sku in skus:
    norm = ""
    for c in sku:
        if check_isalnum(c) is not None:
            norm = norm + (check_isalnum(c))  # creates a new string each loop wasteful

    cleaned_skus.append(norm)

print(cleaned_skus)
"""
# BEST Version that balances clarity, correctness, and cleverness:   senior engineers use instinctively:
#  isolate the invariant, then let the outer structure express the data flow.  “I need a function that normalizes a SKU,
#  and then I apply it to each SKU.”  How clear articulation turns into a roadmap
# When you broke the problem into parts, you implicitly created a pipeline:
# Define the invariant — “A SKU is the uppercase sequence of alphanumeric characters.”
# Identify the inner transformation — “Walk characters, filter noise, normalize signal.”
# Encapsulate that transformation — a helper that handles one SKU or one character.
# Apply it across the dataset — the outer loop or comprehension.
# Once those pieces exist, the final solution isn’t something you “figure out”; 
# it’s something that naturally falls out of the structure you’ve already defined.
"""

def normalize_sku(sku: str):
    chars = []  # 'ABC123' collect pieces in a list
    for c in sku:
        normalized = check_isalnum(c)
        if normalized is not None:
            chars.append(normalized)
            # idiomatic way to build strings.  join them once at the end
    return "".join(chars)

# ['ABC123', 'ABC123', 'ABC123', 'ABC123']
cleaned_skus = [normalize_sku(sku) for sku in skus]
print(cleaned_skus)

"""
Why this is a senior‑level habit : This is exactly how experienced engineers think:
They don’t start with the outer loop.
They don’t start with syntax.
They start by naming the conceptual units.
Then they build the small pieces ++> Then the final structure emerges naturally.
You just walked through that progression.
"""

"""  
Collapse overlapping time intervals
input = [(1, 3), (2, 4), (6, 8), (7, 9)]
output = [(1, 4), (6, 9)]

Real question:  What does “overlap” mean?
What order must the data be in?
What happens with touching intervals like (1,3) and (3,5)?

Observed Assumptions:
each tuple has a lower value, higher value as pattern
seems the higher value of a last tuple needs to be compared to lower value of curr tuple 
and if greater collapse the 2 tuples together keeping lower value of prev tuple and higher value of curr tuple

What “overlap” actually means: (a,b) and (c,d) overlaps if b>=c or c <= b (obvious overlap)
when (1,3) and (3,5) are compared the boundaries "touch" but treat as merge case
when (1,3) and (4,6) are compared there's No overlap so No Merge

BUT comparison assumes tuples are given in sorted order.. sorted tuples is a requirement
the core invariant: 
  current interval → the one you’re building; 
  next interval → the one you’re inspecting;
  overlap rule → next.start ≤ current.end
  merge rule → new end = max(current.end, next.end)
"""
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

# final output append last tuple
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
