import calendar
from cgitb import lookup
from collections import deque
import datetime

# base class for calendar
class BaseCalendarMixin:
    # 0 means it starts from Monday, if you set first_weekday as 6, it starts from Sunday
    # this can be specified in views
    first_weekday = 0
    week_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # to use calendar.Calendar function, create an instance
    def setup_calendar(self):
        self._calendar = calendar.Calendar(self.first_weekday)

    # adjust for first_weekday, shift week_names
    # to do that use deque
    def get_week_names(self):
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names

# class for week calendar
class WeekCalendarMixin(BaseCalendarMixin):
    # return each days in the week
    def get_week_days(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')

        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        
        for week in self._calendar.monthdatescalendar(date.year, date.month):
            # in each week of the month, if the date is included in the week, it must be the week to display
            if date in week:
                return week

    # to get a week information
    def get_week_calendar(self):
        self.setup_calendar()
        days = self.get_week_days()
        first = days[0]
        last = days[-1]
        calendar_data = {
            # today
            'now': datetime.date.today(),
            # every day in the week
            'week_days': days,
            # last week
            'week_previous': first - datetime.timedelta(days=7),
            # next week
            'week_next': first + datetime.timedelta(days=7),
            # a list of day of week
            'week_names': self.get_week_names(),
            # first day of the week
            'week_first': first,
            # last day of the week
            'week_last': last,
        }
        return calendar_data

# class for meal in the week
class WeekWithMealMixin(WeekCalendarMixin):
    # get each day and meals
    def get_week_meals(self, start, end, days):
        lookup = {
            # create date__range: (start, end) dynamically
            'date__range'.format(self.date_field): (start, end)
        }
        # search object betwenn start and end
        queryset = self.model.objects.filter(**lookup)

        # create a dictionary which key is day and value is []
        day_meals = {day: [] for day in days}
        # each meal in queryset, get date and append it to the day_meals
        for meal in queryset:
            meal_date = getattr(meal, self.date_field)
            day_meals[meal_date].append(meal)
        return day_meals
    
    def get_week_calendar(self):
        calendar_context = super().get_week_calendar()
        calendar_context['week_day_meals'] = self.get_week_meals(
            calendar_context['week_first'],
            calendar_context['week_last'],
            calendar_context['week_days']
        )
        return calendar_context