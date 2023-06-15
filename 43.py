def maximumMeetings(start, end):
    n = len(start)
    meet = []

    for i in range(n):
        meet.append({'start': start[i], 'end': end[i], 'pos': i+1})

    meet.sort(key=lambda x: (x['end'], x['pos']))

    ans = []
    finish_time = meet[0]['end']
    ans.append(meet[0]['pos'])

    for i in range(1, n):
        if meet[i]['start'] > finish_time:
            finish_time = meet[i]['end']
            ans.append(meet[i]['pos'])

    return ans