from datetime import datetime, timedelta
raw = ["10:00", "10:10", "10:40", "11:20"]
times = [datetime.strptime(t, "%H:%M") for t in raw]
sessions = []
# init first group in output
current = [times[0]]

# zip to compare consecutive pairs — very Pythonic.
for prev, curr in zip(times, times[1:]):
    if curr - prev <= timedelta(minutes=30):
        current.append(curr)
    else:
        sessions.append(current)
        current = [curr]

sessions.append(current)

print(sessions)