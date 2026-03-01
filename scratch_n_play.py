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
  {"timestamp": "2024-01-01T14:00", "amount": 35}
]
from datetime import date, datetime


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

# convert to a simple list of tuple values?  and I should not assume sorting so I must sort myself


trans_data = [(datetime_str_to_date(d.get("timestamp")), d.get("amount"))
               for d in data]
sorted_data = sorted(trans_data)

#sorted_dict = [{d.get("timestamp")[:10] : d.get("amount")}
#               for d in data]

#  once I have sorted pairs I think i can keep iterating but initialize with a current obj = {date: amounts_list} and
#  as I iterate update the current obj if appropriate or append last current_obj into final output and re-set current obj
# sample sorted_date
# [(datetime.date(2024, 1, 1), 10), (datetime.date(2024, 1, 1), 20), (datetime.date(2024, 1, 1), 35), (datetime.date(2024, 1, 2), 5)]

#curr_date = sorted_data[0]  # initialize before start

def reset_tuple(row: tuple):
    return ( row[0], [row[1]] )

def reset_dict(row: tuple):
    date_str = row[0].strftime("%Y-%m-%d")
    return {date_str: [row[1]]}

grouped_list = []

for idx, sd in enumerate(sorted_data):
    if idx == 0:
        curr_date = reset_tuple(sd)
        curr_dict = reset_dict(sd)  # initialize before start
        continue
    # are we on the same date ?
    if curr_date[0] == sd[0]:
        # re-create curr_date tuple
        #curr_date = ( curr_date[0] , curr_date[1]+[sd[1]] )
        sd_date = sd[0].strftime("%Y-%m-%d")
        curr_dict[sd_date] = curr_dict.get(sd_date) + [sd[1]]

    else:   # save curr_date before reset
        grouped_list.append(curr_dict)
        curr_date = reset_tuple(sd)  # reset with new date
        curr_dict = reset_dict(sd)
    # check for last loop as exit condition
    if idx+1 == len(sorted_data):
        # save last tuple after exit loop
        grouped_list.append(curr_dict)

print(grouped_list)