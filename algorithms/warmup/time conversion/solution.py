time = input().strip()

hour, minute, second = int(time[0:2]), time[3:5], time[6:8]
if (hour != 12 and time[-2] == 'P') or (hour == 12 and time[-2] == 'A'):
    hour = (hour + 12) % 24

print('{0:02d}:{1}:{2}'.format(hour, minute, second))