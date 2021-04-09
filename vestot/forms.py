from django import forms
from .models import VesetModel
from zmanim.hebrew_calendar.jewish_date import JewishDate

ona_choice = [(0, 'יום'), (1, 'לילה')]

class FastCalculatorForm(forms.Form):

    year = forms.ChoiceField(label='בחר שנה', 
                                choices=[(i,'') for i in range(5770, 5870)],
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'year'}))
    month = forms.ChoiceField(label='בחר חודש', 
                                choices=[(i,'') for i in range(1, 14)],
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'month'}))
    day = forms.ChoiceField(label='בחר יום',
                                choices=[(i,'') for i in range(1, 31)],
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'day'}))

    ona = forms.ChoiceField(label='בחר עונה', 
                                choices=ona_choice, 
                                widget=forms.Select(attrs={'class': 'form-select', 'id': 'ona'}))
    
    afl = forms.IntegerField(label='בחר הפלגה (לא חובה)', min_value=1, required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
class AddVesetForm(forms.ModelForm):
    class Meta:
        model = VesetModel
        fields = ('year', 'month', 'day', 'ona',)
    
    def __init__(self, *args, **kwargs):
        super(AddVesetForm, self).__init__(*args, **kwargs)
        
        self.fields['year'].widget = forms.Select(attrs={'class': 'form-select', 'id': 'year'}, choices=[(i,'') for i in range(5770, 5870)])
        self.fields['year'].label = 'בחר שנה'

        self.fields['month'].widget = forms.Select(attrs={'class': 'form-select', 'id': 'month'}, choices=[(i,'') for i in range(1, 14)])
        self.fields['month'].label = 'בחר חודש'

        self.fields['day'].widget = forms.Select(attrs={'class': 'form-select', 'id': 'day'}, choices=[(i,'') for i in range(1, 31)])
        self.fields['day'].label = 'בחר יום'

        self.fields['ona'].widget = forms.Select(attrs={'class': 'form-select'}, choices=ona_choice)
        self.fields['ona'].label = 'בחר עונה'