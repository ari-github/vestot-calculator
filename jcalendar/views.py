from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from zmanim.hebrew_calendar.jewish_date import JewishDate

from .hebrew_date_formatter import HebrewDateFormatter
hdf = HebrewDateFormatter()

def month_view(request, year, month):
    jd = JewishDate(year, month, 1)

    return render(request, 'calendar/month.html', {
        'day_list': get_month_data(jd),
        'prev_month': get_prev(jd),
        'next_month': get_next(jd),
        'heb_year': hdf.format_hebrew_number(jd.jewish_year),
        'heb_month': hdf.format_month(jd),

        })

def calendar_home_view(request):
    jd = JewishDate()
    return HttpResponseRedirect(reverse('calendar-month', args=[jd.jewish_year, jd.jewish_month]))


def get_month_data(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, 1)
    day_of_week = jd.day_of_week
    days_in_month = jd.days_in_jewish_month()
    
    data = {}
    for i in range(1, 36):
        if i < day_of_week or i > days_in_month:
            data[i] = {}
        else:
            data[i] = {
                'date': jd,
                'heb_year': hdf.format_hebrew_number(jd.jewish_year),
                'heb_month': hdf.format_month(jd),
                'heb_day': hdf.format_hebrew_number(jd.jewish_day),
            }
            jd.forward()
    return data

def get_prev(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, jd.jewish_day)
    jd.back(1)
    return [jd.jewish_year, jd.jewish_month]

def get_next(jd):
    jd = JewishDate(jd.jewish_year, jd.jewish_month, jd.jewish_day)
    jd.forward(jd.days_in_jewish_month())
    return (jd.jewish_year, jd.jewish_month)
