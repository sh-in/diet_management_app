import calendar
from collections import deque
import datetime

class BaseCalendarMixin:
    first_weekday = 0
    week_names = ["月", "火", "水", "木", "金", "土", "日"]

    def setup_calendar(self):
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names

class WeekCalendarMixin(BaseCalendarMixin):
    def get_week_days(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')

        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        
        for week in self._calendar.monthdatescalendar(date.year, date.month):
            if date in week:
                return week

    def get_week_calendar(self):
        self.setup_calendar()
        days = self.get_week_days()
        first = days[0]
        last = days[-1]
        calendar_data = {
            'now': datetime.date.today(),
            'week_days': days,
            'week_previous': first - datetime.timedelta(days=7),
            'week_next': first + datetime.timedelta(days=7),
            'week_names': self.get_week_names(),
            'week_first': first,
            'week_last': last,
        }
        return calendar_data