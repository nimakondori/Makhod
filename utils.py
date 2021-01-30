from datetime import datetime

from pytz import timezone, utc

anniversary = datetime(2021, 2, 6, 0, 0 ,0).strftime('%Y-%m-%d')
zone = "Amercia/Vancouver"


def count_down(tz: timezone) -> dict:
    """ Function return days and time to next new year """
    ANNIVERSARY_MONTH = 2
    ANNIVERSARY_DAY = 6
    tz = timezone(tz)
    print (tz)
    anniversary = datetime(datetime.now(tz).year, ANNIVERSARY_MONTH, ANNIVERSARY_DAY, 0, 0,0,0)
    today = datetime.now()
    if today > anniversary:
        anniversary = datetime(datetime.now().year + 1, ANNIVERSARY_MONTH ,ANNIVERSARY_DAY ,0, 0, 0,0)
    # print(anniversary, today)
    timedelta = anniversary - today
    seconds_in_day = 24 * 60 * 60
    print("anniversary ", anniversary)
    print("today =",today)
    print(divmod(timedelta.days * seconds_in_day + timedelta.seconds, 60))
    # print(timedelta)
    duration_in_s = timedelta.total_seconds()
    total_days = divmod(duration_in_s, 86400)  # Get days (without [0]!)
    hour_diff = divmod(total_days[1], 3600)  # Use remainder of days to calc hours
    minute_diff = divmod(hour_diff[1], 60)  # Use remainder of hours to calc minutes
    sec_diff = divmod(minute_diff[1], 1)  # Use remainder of minutes to calc seconds
    print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (
    total_days[0], hour_diff[0], minute_diff[0], sec_diff[0]))

    return {
        "day": str(int(total_days[0])),
        "hour": str(int(hour_diff[0])),
        "min": str(int(minute_diff[0])),
        "sec": str(int(sec_diff[0])),
    }