def time(hour_minute):
    hours = int(hour_minute / 60)
    minutes = hour_minute % 60
    if (hours == 1):
        hours = str(hours) + " Hour"
    else:
        hours = str(hours) + " Hours"
    if (minutes == 1):
        minutes = str(minutes) + " Minute"
    else: 
        minutes = str(minutes) + " Minutes"
        
    hour_minute = hours + ', ' + minutes
    return hour_minute

time(hour_minute)