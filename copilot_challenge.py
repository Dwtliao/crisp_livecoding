"""
full-system challenge that uses everything
This is the one that will push you into the “I’m actually ready” zone.

 Main Problem: Group, Merge, and Reconstruct
You’re given a list of transaction fragments. Each fragment has:

    => user_id, timestamp , amount , category

But the list is unsorted, and each user may appear many times.

Your task:  Return a dict mapping each user_id to a list of that user’s transactions,
        sorted by timestamp,
        with duplicate timestamps removed (keep the latest amount).

expected output :
{
  1: [
    {"timestamp": 20, "amount": 3, "category": "food"},
    {"timestamp": 50, "amount": 10, "category": "travel"},
  ],
  2: [
    {"timestamp": 90, "amount": 2, "category": "misc"},
    {"timestamp": 100, "amount": 7, "category": "food"},  # deduped, kept latest
  ]
}

Observations & questions:  final output has each user id value as KEY
we need to stare each user's transactions in a dicty using user-id as KEY and update each KEY value
HOWEVER:  look for duplicate timestamps
    likely easiest is to also store each timestamp as a key whose transaction list can be updated
"""

transactions = [
  {"user_id": 2, "timestamp": 100, "amount": 5, "category": "food"},
  {"user_id": 1, "timestamp": 50, "amount": 10, "category": "travel"},
  {"user_id": 2, "timestamp": 100, "amount": 7, "category": "food"},  # duplicate timestamp same as row 1
  {"user_id": 1, "timestamp": 20, "amount": 3, "category": "food"},
  {"user_id": 2, "timestamp": 90, "amount": 2, "category": "misc"},
]

# step 1: read raw data and group transactions by user_id ; keeping only timestamp, amount, category


def group_user_data(raw_data):
    user_trans = {}

    for row in raw_data:
        user_id = row.get("user_id")
        trans_row = {k: v for k, v in row.items() if k != "user_id"}    # keep only transaction details
        user_trans.setdefault(user_id, []).append(trans_row)

    return user_trans

trans_by_user = group_user_data(raw_data=transactions)
print(trans_by_user)
# need to sort trans_by_user in ascending order; sorted uses key of items()
trans_by_user = dict(sorted(trans_by_user.items()))

def clean_user_data(data):
    output = {}
    for k, v in data.items():   # loop thru trans per user
        user_trans = {}
        for t in v:     # use time as key so last transaction by time of user is kept
            time = t.get("timestamp")
            user_trans[time] = t

        # must sort by timestamp as part of output per user
        output[k] = sorted(list(user_trans.values()), key=lambda r: r["timestamp"])

    return output

output = clean_user_data(trans_by_user)
print(output)

# simpler one pass solution
def group_and_clean(transactions):
    grouped = {}

    for row in transactions:
        uid = row["user_id"]
        grouped.setdefault(uid, {})
        ts = row["timestamp"]
        grouped[uid][ts] = {
            "timestamp": ts,
            "amount": row["amount"],
            "category": row["category"],
        }

    output = {}
    for uid, ts_map in grouped.items():
        output[uid] = sorted(ts_map.values(), key=lambda r: r["timestamp"])

    return output


