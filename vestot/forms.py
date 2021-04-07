from django import forms
from .models import VesetModel
from zmanim.hebrew_calendar.jewish_date import JewishDate

year_choice = [(5779, 'תשע"ט'), (5780, 'תש"פ'), (5781, 'תשפ"א'), (5782, 'תשפ"ב'), (5783, 'תשפ"ג'),]
month_choice = [(7, 'תשרי'), (8, 'חשוון'), (9, 'כסלו'), (10, 'טבת'), (11, 'שבט'), (12, 'אדר'), (13, 'אדר ב'), (1, 'ניסן'), (2, 'אייר'), (3, 'סיון'), (4, 'תמוז'), (5, 'אב'), (6, 'אלול'),]
day_choice = [(1, 'א'), (2, 'ב'), (3, 'ג'), (4, 'ד'), (5, 'ה'), (6, 'ו'), (7, 'ז'), (8, 'ח'), (9, 'ט'), (10, 'י'), (11, 'יא'), (12, 'יב'), (13, 'יג'), (14, 'יד'), (15, 'טו'), (16, 'טז'), (17, 'יז'), (18, 'יח'), (19, 'יט'), (20, 'כ'), (21, 'כא'), (22, 'כב'), (23, 'כג'), (24, 'כד'), (25, 'כה'), (26, 'כו'), (27, 'כז'), (28, 'כח'), (29, 'כט'), (30, 'ל'), ]
ona_choice = [(0, 'יום'), (1, 'לילה')]

class FastCalculatorForm(forms.Form):
    select_widget = forms.Select(attrs={'class': 'form-select'})
    jd = JewishDate()
    year = forms.ChoiceField(label='בחר שנה', choices=year_choice, widget=select_widget, initial=jd.jewish_year)
    month = forms.ChoiceField(label='בחר חודש', choices=month_choice, widget=select_widget, initial=jd.jewish_month)
    day = forms.ChoiceField(label='בחר יום', choices=day_choice, widget=select_widget, initial=jd.jewish_day)
    ona = forms.ChoiceField(label='בחר עונה', choices=ona_choice, widget=select_widget)

    afl = forms.IntegerField(label='בחר הפלגה (לא חובה)', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AddVesetForm(forms.ModelForm):
    class Meta:
        model = VesetModel
        fields = ('year', 'month', 'day', 'ona',)
    
    def __init__(self, *args, **kwargs):
        super(AddVesetForm, self).__init__(*args, **kwargs)
        jd = JewishDate()
        
        self.fields['year'].widget = forms.Select(attrs={'class': 'form-select'}, choices=year_choice)
        self.fields['year'].label = 'בחר שנה'
        self.fields['year'].initial = jd.jewish_year

        self.fields['month'].widget = forms.Select(attrs={'class': 'form-select'}, choices=month_choice)
        self.fields['month'].label = 'בחר חודש'
        self.fields['month'].initial = jd.jewish_month

        self.fields['day'].widget = forms.Select(attrs={'class': 'form-select'}, choices=day_choice)
        self.fields['day'].label = 'בחר יום'
        self.fields['day'].initial = jd.jewish_day

        self.fields['ona'].widget = forms.Select(attrs={'class': 'form-select'}, choices=ona_choice)
        self.fields['ona'].label = 'בחר עונה'