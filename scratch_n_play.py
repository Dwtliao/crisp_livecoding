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

from datetime import datetime

def find_consec_days_slice(strings):
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
