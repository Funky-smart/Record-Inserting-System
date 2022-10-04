from django.forms import ModelForm
from .models import Directory


class TelephoneForm(ModelForm):
    class Meta:
        model = Directory
        exclude = ['date_created', 'date_updated']