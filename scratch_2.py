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