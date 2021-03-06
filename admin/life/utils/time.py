import pytz

from calendar import monthrange
from datetime import date, datetime, timedelta
from time import mktime

from django.conf import settings


def utc_to_local_time(dt):
    """
    接受一个utc时间参数或者一个时间列表，返回一个本地
    时区的时间或者时间列表(参数和返回值都为datetime类型)
    """
    tz = pytz.timezone(settings.TIME_ZONE)

    utc_to_local = lambda x: x.astimezone(tz) if x.tzinfo else tz.localize(x)

    if isinstance(dt, (str, )):
        for fmt in ('%Y-%m-%d', '%Y-%m-%d %H:%M:%S'):
            try:
                dt = datetime.strptime(dt, fmt)
                return utc_to_local(dt)
            except ValueError:
                pass
        raise ValueError('no valid date format found')
    elif isinstance(dt, (list, tuple)):
        return [utc_to_local_time(i) for i in dt]
    elif type(dt) is date:
        dt = datetime.combine(dt, datetime.min.time())
    elif type(dt) is datetime:
        pass
    else:
        raise TypeError

    return utc_to_local(dt)


def date_format(time):
    return utc_to_local_time(time).strftime(pattern)


def get_months(self):
    minus = lambda x, y: (x + relativedelta(months=y))
    today = datetime.now().replace(day=1)
    return list(map(lambda x: [minus(today, x-11), minus(today, x-10)], range(0, 12)))


def get_week(self):
    minus = lambda x, y: (x + timedelta(days=y)).strftime('%Y-%m-%d %H:%M:%S')
    today = datetime.now()
    return list(map(lambda x: minus(today, x-6), range(0, 7)))


def get_days(self):
    minus = lambda x, y: (x + timedelta(days=y))
    today = datetime.now()
    return list(map(lambda x: [minus(today, x-31), minus(today, x-30),], range(0, 31, 2)))
