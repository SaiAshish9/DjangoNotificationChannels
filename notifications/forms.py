from django import forms
from models import Score

# Create your models here.

class ScoreForm(forms.ModelForm):
    model = Score
    fields = ["score"]
    