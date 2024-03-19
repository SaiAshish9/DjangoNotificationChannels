from django.shortcuts import render

from forms import ScoreForm

# Create your views here.

def index(request):
    form = ScoreForm()
    return render(request, 'index.html', { form: form })