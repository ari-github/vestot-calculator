from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from zmanim.hebrew_calendar.jewish_date import JewishDate

# Create your views here.
def month(request, year, month):
    jd = JewishDate(year, month, 1)
    day_list = get_month_data(jd)

    return render(request, 'calendar/month.html', {
        'day_list': day_list,
        'prev_month': get_prev(jd),
        'next_month': get_next(jd),

        })


def calendar_home(request):
    jd = JewishDate()
    return HttpResponseRedirect(reverse('calendar-month', args=[jd.jewish_year, jd.jewish_month]))

def get_month_data(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, 1)
    day_list = [JewishDate(jd.jewish_year, jd.jewish_month, day+1) for day in range(jd.days_in_jewish_month())]
    print(day_list[0].day_of_week -1)
    day_list = ['']* (day_list[0].day_of_week -1) + day_list + ['']* (day_list[-1].day_of_week -1)
    print(day_list)

    day_list = [day_list[(i-1)*7: i*7] for i in range(1, len(day_list) // 7 + 1)]
    return day_list

def get_prev(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, jd.jewish_day)
    jd.back(1)
    return [jd.jewish_year, jd.jewish_month]

def get_next(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, jd.jewish_day)
    jd.forward(jd.days_in_jewish_month())
    return (jd.jewish_year, jd.jewish_month)
