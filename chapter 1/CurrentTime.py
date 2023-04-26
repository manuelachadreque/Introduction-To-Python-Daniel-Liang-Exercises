import time

seconds = time.time()

totalSeconds = int(seconds)

#Get the current second
currentSeconds = totalSeconds % 60

#Get the total minutes

totalMinutes = totalSeconds // 60

#Get the current minutes
currentMinute = totalMinutes % 60

# Get total hours

totalHours = totalMinutes // 60

# Get Current hour

currentHour = totalHours % 24


print(currentHour, ":", currentMinute, ":", currentSeconds)
