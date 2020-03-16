from django.shortcuts import render
from . import forms


# Create your views here.
def form_name_view(request):
    form = forms.FormName()
    return render(request, 'forms_app/form_page.html', {'form': form})
