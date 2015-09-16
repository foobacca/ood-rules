from __future__ import unicode_literals, absolute_import

from datetime import datetime, timedelta


def is_weekday(day):
    # 0 is Monday, 4 is Friday
    return day.weekday() < 5


def convert_date(date_string):
    """ the date strings are generally like '08/18/2014 13:00:00 GMT' """
    return datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S %Z')


def halfday_str(day, am_pm):
    return day.isoformat() + '-' + am_pm


def xhalfdays(start, end):
    """ generator: takes two datetimes, and produces strings like:
        2015-05-28-am
        2015-05-28-pm
        2015-05-29-am
        2015-05-29-pm

    Note it should skip weekends
    """
    start_am_pm = 'am' if start.hour < 12 else 'pm'
    end_am_pm = 'am' if end.hour < 14 else 'pm'
    day = start.date()
    end_day = end.date()
    one_day = timedelta(days=1)

    if start_am_pm == 'pm':
        if is_weekday(day):
            yield halfday_str(day, 'pm')
        day += one_day

    while day < end_day:
        if is_weekday(day):
            yield halfday_str(day, 'am')
            yield halfday_str(day, 'pm')
        day += one_day

    if day == end_day and is_weekday(day):
        yield halfday_str(day, 'am')
        if end_am_pm == 'pm':
            yield halfday_str(day, 'pm')


def xhalfdays_for_day(day):
    day = day.date()
    yield halfday_str(day, 'am')
    yield halfday_str(day, 'pm')


def _find_key_label_from_label_list(label_list, key):
    key_label_list = [d.get(key) for d in label_list]
    # filter out falsy values
    key_label_list = filter(None, key_label_list)
    if key_label_list:
        return key_label_list[0]
    else:
        return None


def find_any_label_from_label_list(label_list):
    """
    We expect label_list to be:

    [
        {u'short': u'', u'full': u''},
        {u'short': u'Hamish', u'full': u'Hamish'},
        {u'short': u'', u'full': u''}
    ]
    """
    label = _find_key_label_from_label_list(label_list, 'full')
    if label:
        return label
    label = _find_key_label_from_label_list(label_list, 'short')
    return label
