from .forms import AdForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Ad

def home(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdForm()
    
    ads = Ad.objects.all()
    total_cost = sum(ad.spend for ad in ads)
    total_cost_sharing = sum(ad.ads_run * ad.spend for ad in ads)
    total_reimbursement = total_cost_sharing / 2

    for ad in ads:
        ad.cost_sharing = ad.ads_run * ad.spend
        ad.reimbursement = ad.cost_sharing / 2

    context = {
        'form': form,
        'ads': ads,
        'total_cost': total_cost,
        'total_cost_sharing': total_cost_sharing,
        'total_reimbursement': total_reimbursement,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ad_reimbursement_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'ad_reimbursement_app/login.html'