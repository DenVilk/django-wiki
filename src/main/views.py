from django.shortcuts import render
from .utils import Currency, Contests
from markdown import markdown

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'text': markdown('*HEEEEEEEEEELP*')})