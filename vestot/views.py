from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from zmanim.hebrew_calendar.jewish_date import JewishDate

from .forms import AddVesetForm, FastCalculatorForm
from .models import VesetModel
from . import vestot

# Create your views here.

def home(request):
    context = {}
    if request.user.is_authenticated:
        ves = VesetModel.objects.filter(user=request.user)
        vsetot_list = vestot.vestot_calculator([v.year, v.month, v.day, v.ona] for v in ves)
        
        veset_model = [ves.filter(year=veset[0].year, 
                                month=veset[0].month, 
                                day=veset[0].day, 
                                ona=veset[0].ona).first()
                                for key, veset in enumerate(vsetot_list)]
        context['vsetot_list'] = zip(vsetot_list, veset_model)

    return render(request, 'vestot/home.html', context)

class AddVeset(CreateView):
    model = VesetModel
    form_class = AddVesetForm
    template_name = 'vestot/add_veset.html'

    def form_valid(self, form):
        veset = form.save(commit=False)
        veset.user = self.request.user
        VesetModel.objects.get_or_create(year=veset.year, month=veset.month, day=veset.day, ona=veset.ona, user=veset.user)
        return HttpResponseRedirect(reverse('home'))


def delete_veset(request, num):
    ves_model = VesetModel.objects.get(pk=num)
    
    if request.method == 'POST':
        ves_model.delete()
        return HttpResponseRedirect(reverse('home'))
        
    else:
        veset = vestot.Veset(ves_model.year, ves_model.month, ves_model.day, ves_model.ona)
        return render(request, 'vestot/delete_veset.html', {
            'veset': veset,
            'ves_model': ves_model,
            })

def fast_calculator(request):
    if request.method == 'POST':
        form = FastCalculatorForm(request.POST)
        if form.is_valid():
            vestot_list = vestot.fast_vestot_calculator(
                            int(form.cleaned_data['year']),
                            int(form.cleaned_data['month']),
                            int(form.cleaned_data['day']),
                            int(form.cleaned_data['ona']),
                            form.cleaned_data['afl']
                        )
            return render(request, 'vestot/fast_calculator.html', {'vestot_list': vestot_list})

    form = FastCalculatorForm()
    return render(request, 'vestot/fast_calculator.html', {'form': form})