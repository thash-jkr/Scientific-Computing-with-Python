def add_time(start, duration, dday=None):
    mer = start[-2:]
    day = 0
    d = {
        'Sunday': 1,
        'Monday': 2,
        'Tuesday': 3,
        'Wednesday': 4,
        'Thursday': 5,
        'Friday': 6,
        'Saturday': 7
    }
    new_time = ""
    start_hour = int(start[:-3].split(':')[0])
    start_min = int(start[:-3].split(':')[1])
    hour = int(duration.split(':')[0])
    minu = int(duration.split(':')[1])
    if mer == 'AM':
        res_hour = start_hour + hour
        res_min = start_min + minu
        if res_min >= 60:
            res_hour += 1
            res_min -= 60
        if res_min < 10:
          res_min = '0' + str(res_min)
    elif mer == 'PM':
        res_hour = 12 + start_hour + hour
        res_min = start_min + minu
        if res_min >= 60:
            res_hour += 1
            res_min -= 60
        if res_min < 10:
          res_min = '0' + str(res_min)
    if res_hour >= 24:
        day = res_hour // 24
        res_hour = res_hour % 24
        #state = f"({str(day)} days later)"
    if res_hour >= 12:
        res_mer = 'PM'
        if res_hour > 12:
          res_hour -= 12
    else:
        res_mer = 'AM'
    if dday:
        dday = dday.capitalize()
        day_num = d[dday]
        if day > 0:
            new_day = day + day_num
            while new_day > 7:
                new_day = new_day - 7
            new_day = [k for (k, v) in d.items() if v == new_day][0]
        else:
          new_day = dday

    if res_hour == 0:
      res_hour = 12
    new_time += f'{str(res_hour)}:{res_min} {res_mer}'
    if dday:
      new_time += f', {new_day}'
    if day > 0:
      if day == 1:
        new_time += f' (next day)'
      else:
        new_time += f' ({day} days later)'
    return new_time