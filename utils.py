from datetime import datetime

from pytz import timezone, utc

anniversary = datetime(2021, 2, 6, 0, 0 ,0).strftime('%Y-%m-%d')
zone = "Amercia/Vancouver"


def count_down(tz: timezone) -> tuple:
    """ Function return days and time to next new year """

    tz = timezone(tz)
    anniversary = datetime(datetime.now(tz).year, 1, 23, 10, 43, tzinfo=tz)
    today = datetime.now(tz)
    timedelta = today - anniversary
    if timedelta.seconds > 0:
        anniversary = datetime(datetime.now(tz).year + 1, 1, 23,10, 43)
    print(anniversary)

    day_diff = anniversary.day - today.day
    if day_diff < 0:
        day_diff = 30 + anniversary.day - today.day
    month_diff = anniversary.month - today.month - 1
    if month_diff < -1:
        month_diff += 12
    elif month_diff == -1:
        month_diff = 0

    total_days = int(day_diff + ((month_diff / 2) * 30) + ((month_diff / 2) * 31))

    hour_diff = anniversary.hour - today.hour
    if hour_diff < 0:
        hour_diff = (anniversary.hour - today.hour) + 23

    minute_diff = anniversary.minute - today.minute
    if minute_diff < 0:
        minute_diff = 59 + anniversary.minute - today.minute

    sec_diff = anniversary.second - today.second
    if sec_diff < 0:
        sec_diff = 59 + (anniversary.second - today.second)
    print(month_diff, day_diff, hour_diff, minute_diff, sec_diff)
    return {
        "day": str(total_days).zfill(2),
        "hour": str(hour_diff).zfill(2),
        "min": str(minute_diff).zfill(2),
        "sec": str(sec_diff).zfill(2),
    }