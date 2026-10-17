
def schedule_events(events):
    events.sort(key=lambda event: event[2])

    selected = []
    last_end = -1

    for event in events:
        if event[1] >= last_end:
            selected.append(event)
            last_end = event[2]

    return selected


events = [
    ("Meeting", 9, 10),
    ("Workshop", 9, 12),
    ("Lecture", 10, 11),
    ("Project Work", 11, 13),
    ("Interview", 13, 14),
    ("Seminar", 12, 15)
]

scheduled = schedule_events(events)

print("Scheduled Calendar Events:")
for name, start, end in scheduled:
    print(name, "-", start, "to", end)

