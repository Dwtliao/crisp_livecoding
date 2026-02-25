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

# example 2
rows = [ {"id": 1, "version": 1}, {"id": 1, "version": 3}, {"id": 1, "version": 2}, ]
latest_row = max(rows, key=lambda r: r["version"])
print(latest_row)

scores = { "alice": 12, "bob": 7, "charlie": 19, "diana": 14 }
winner = max(scores.items(), key=lambda kv: kv[1])
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

