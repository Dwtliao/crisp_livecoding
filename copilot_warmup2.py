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

"""  
Extract unique domains from email addresses
emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
unique_domains = ["gmail.com", "yahoo.com"]

Assumptions: the pattern seems to be the internet domain name appears after symbol "@"
we dont need to know what is before '@' but we want all chars after '@' symbol seems to be essence of problem
Helper funcs:  something to find the position of string where '@' appears
"""
emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
emails_recurr = ["dwtliao@_@yahoo.com", "bob@yahoo.com"]

def find_domain_start_simple(search_char: str, email: str):
    # str.find() returns -1 if not found.
    position = email.find(search_char)
    if position != -1:
        return position
    return None

def extract_domain(email: str):
    start = find_domain_start_simple('@', email)
    if start is not None:
        return email[start + 1:]
    else:
        return None

# we want unique email domains so use a set to store
unique_domains = set( extract_domain(email) for email in emails )
print((unique_domains))

# what if search char @ occurrs multiple times? we want the domain after final @ char, good case for recursion
# why this works, You never slice the string always search the original entire email and move start_index forward
def find_domain_start_recurr(search_char: str, email: str, start_index=0, last_position=None):
    # Find next occurrence starting from start_index
    position = email.find(search_char, start_index)

    if position == -1:  # ending condition of recursion
        return last_position

    # Found an '@', update last_position thru all recurrsive calls
    last_position = position

    # Recursive call to search for another '@' after this one
    return find_domain_start_recurr(search_char, email, position + 1, last_position)

def extract_domain2(email: str):
    start = find_domain_start_recurr('@', email, None)
    if start is not None:
        return email[start + 1:]
    else:
        return None

unique_recurr = set(extract_domain2(email) for email in emails_recurr )
print(unique_recurr)

# really simplified elegant solution
unique_domains = {
    email.split('@')[1].lower()
    for email in emails
    if '@' in email
}
print(unique_domains)

"""
Section 2 “Don’t code until you see the structure”
Group transactions by day

data = [
  {"timestamp": "2024-01-01T10:00", "amount": 10},
  {"timestamp": "2024-01-01T12:00", "amount": 20},
  {"timestamp": "2024-01-02T09:00", "amount": 5}
]
wanted_output = {
  "2024-01-01": [10, 20],
  "2024-01-02": [5]
}
Observed Assumptions to start: each row of data is a dict obj of a date and timestamp key and amount key
we dont need the time port of datetime so we need to func to convert these values and drop the time component

once data list is converted to date keys with amounts it will be easier to group amount transactions together
"""
data = [
  {"timestamp": "2024-01-01T10:00", "amount": 10},
  {"timestamp": "2024-01-01T12:00", "amount": 20},
  {"timestamp": "2024-01-02T09:00", "amount": 5},
  {"timestamp": "2024-01-01T14:00", "amount": 35},
  {"timestamp": "2024-01-02T12:00", "amount": 55}
]
from datetime import date, datetime

# convert to a simple list of tuple values?  and I should not assume sorting so I must sort myself
def datetime_str_to_date(dt_str: str):
    """
    Convert an ISO-like datetime string (e.g., '2024-01-01T10:00') to a date object.
    """
    try:
        # Parse the datetime string
        dt_obj = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
        return dt_obj.date()
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: {e}")

# sample sorted_date
# [(datetime.date(2024, 1, 1), 10), (datetime.date(2024, 1, 1), 20), (datetime.date(2024, 1, 1), 35), (datetime.date(2024, 1, 2), 5)]


def sort_convert_data(data_in):
    trans_data = [(datetime_str_to_date(d.get("timestamp")), d.get("amount"))
                  for d in data_in]
    return sorted(trans_data)

def reset_dict(date_key, value):
    return {date_key: [value]}


def group_transactions(sorted_data):
    grouped_list = []

    for idx, sd in enumerate(sorted_data):
        sd_date = sd[0].strftime("%Y-%m-%d")
        amt_value = sd[1]
        if idx == 0:
            current_key = sd_date
            curr_dict = reset_dict(sd_date, amt_value)  # initialize before start
            continue

        # are we on the same date ?
        if current_key == sd_date:
            curr_dict[sd_date] = curr_dict.get(sd_date) + [amt_value]

        else:
            grouped_list.append(curr_dict)  # save curr_date before reset
            current_key = sd_date           # start of new data
            curr_dict = reset_dict(current_key, amt_value)

        # check for last loop as exit condition
        if idx+1 == len(sorted_data):
            # save last tuple after exit loop
            grouped_list.append(curr_dict)

    return grouped_list

data_sorted = sort_convert_data(data)
trans_grouped = group_transactions(data_sorted)
print(trans_grouped)