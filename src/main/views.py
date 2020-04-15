from django.shortcuts import render
from .utils import Currency, Contests

# Create your views here.
def index(request):
    usd = Currency(145)
    usd_val = usd['value']
    usd_count = usd['scale']
    eur = Currency(292)
    eur_val = eur['value']
    eur_count = eur['scale']
    rub = Currency(298)
    rub_val = rub['value']
    rub_count = rub['scale']
    uah = Currency(290)
    uah_val = uah['value']
    uah_count = uah['scale']

    contests = Contests()
    contests.reverse()

    return render(request, 'main/index.html', {'usd':usd_val, 'eur':eur_val, 'rub':rub_val, 'uah':uah_val,
                                               'usdc':usd_count, 'eurc':eur_count, 'rubc':rub_count, 'uahc':uah_count,
                                               'contests':contests})