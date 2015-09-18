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

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (
            self.day < other.day or (
                self.day == other.day and
                self.am and other.pm
            )
        )

    def __gt__(self, other):
        return (
            self.day > other.day or (
                self.day == other.day and
                self.pm and other.am
            )
        )

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other


class HalfDayIterator(object):

    def from_start_date(self, date_time, weekday):
        am_pm = 'am' if date_time.hour < 12 else 'pm'
        halfday = HalfDay(date_time.date(), am_pm)
        if weekday and not halfday.is_weekday():
            halfday = halfday.increment_weekday()
        return halfday

    def from_end_date(self, date_time):
        am_pm = 'am' if date_time.hour < 14 else 'pm'
        return HalfDay(date_time.date(), am_pm)

    def from_start_end(self, start, end, weekday=False):
        return (self.from_start_date(start, weekday), self.from_end_date(end))

    def xhalfdays(self, start, end):
        half_day, end_half_day = self.from_start_end(start, end, weekday=True)
        while half_day <= end_half_day:
            yield unicode(half_day)
            half_day = half_day.increment_weekday()

    def xhalfdays_for_day(self, day):
        day = day.date()
        yield unicode(HalfDay(day, HalfDay.AM))
        yield unicode(HalfDay(day, HalfDay.PM))
