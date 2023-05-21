from datetime import date, timedelta
import datetime

def get_week_days(year, week):
    year_start = date(year, 1, 1)
    week_start = year_start + timedelta(days=-year_start.isoweekday(), weeks=week)
    week_end = week_start + timedelta(days=6)
    return week_start, week_end

dt = str(date.today()).split('-')
a, b = get_week_days(2023, date(int(dt[0]), int(dt[1]), int(dt[2])).isocalendar().week)
a = str(a).split('-')
b = str(b).split('-')
after=datetime.datetime(int(a[0]), int(a[1]), int(a[2])-3)
before=datetime.datetime(int(b[0]), int(b[1]), int(b[2])-1)
print(after, before)