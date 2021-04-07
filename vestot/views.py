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
    vestot_adapter = []

    if request.user.is_authenticated:
        ves = VesetModel.objects.filter(user=request.user)
        vestot_list = [vestot.Veset(v.year, v.month, v.day, v.ona) for v in ves]
        vestot_list.sort()

        for key, veset in enumerate(vestot_list):
            forbiden = []
            forbiden.append(veset)
            forbiden.append(vestot.VesetMonth(veset))
            forbiden.append(vestot.VesetMedium(veset))
            forbiden.append(vestot.VesetMediumR(veset))
            if len(vestot_adapter) > 0:
                forbiden.append(vestot.VesetAfl(vestot_adapter[-1][0], veset))
            else:
                forbiden.append('')
            forbiden.append(ves[key])

            vestot_adapter.append(forbiden)

    return render(request, 'vestot/home.html', {
        'vestot_adapter': vestot_adapter
    })

class AddVeset(CreateView):
    model = VesetModel
    form_class = AddVesetForm
    template_name = 'vestot/add_veset.html'

    def form_valid(self, form):
        veset = form.save(commit=False)
        veset.user = self.request.user
        veset.save() 
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