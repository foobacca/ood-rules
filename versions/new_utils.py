from datetime import timedelta


class HalfDay(object):
    one_day = timedelta(days=1)
    AM = 'am'
    PM = 'pm'

    def __init__(self, day, am_pm):
        self.day = day
        self.am_pm = am_pm

    @property
    def am(self):
        return self.am_pm == self.AM

    @property
    def pm(self):
        return self.am_pm == self.PM

    def increment(self):
        if self.pm:
            return HalfDay(self.day + self.one_day, self.AM)
        else:
            return HalfDay(self.day, self.PM)

    def increment_weekday(self):
        halfday = self.increment()
        while not halfday.is_weekday():
            halfday = halfday.increment()
        return halfday

    def is_weekday(self):
        return self.day.weekday() < 5

    def __unicode__(self):
        return '{}-{}'.format(self.day.isoformat(), self.am_pm)

    def __eq__(self, other):
        return self.day == other.day and self.am_pm == other.am_pm

    def __lte__(self, other):
        if self.day < other.day:
            return True
        elif self.day > other.day:
            return False
        # from here on, the days are equal
        elif self.am_pm == other.am_pm or self.am and other.pm:
            return True
        else:
            return False


class HalfDayIterator(object):

    def from_start_date(self, date_time):
        am_pm = 'am' if date_time.hour < 12 else 'pm'
        return HalfDay(date_time.date(), am_pm)

    def from_end_date(self, date_time):
        am_pm = 'am' if date_time.hour < 14 else 'pm'
        return HalfDay(date_time.date(), am_pm)

    def from_start_end(self, start, end):
        return (self.from_start_date(start), self.from_end_date(end))

    def xhalfdays(self, start, end):
        half_day, end_half_day = self.from_start_end(start, end)
        while half_day <= end_half_day:
            yield unicode(half_day)
            half_day = half_day.increment_weekday()

    def xhalfdays_for_day(self, day):
        day = day.date()
        yield unicode(HalfDay(day, HalfDay.AM))
        yield unicode(HalfDay(day, HalfDay.PM))
