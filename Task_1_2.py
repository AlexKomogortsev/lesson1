# Task 2

time = int(input("Enter number of secs:"))
hours = time // 3600
mins = (time % 3600) // 60
secs = (time % 3600) % 60
print('%02d:%02d:%02d' % (hours, mins, secs))

input("Press Enter")