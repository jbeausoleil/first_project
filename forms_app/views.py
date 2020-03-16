from django.shortcuts import render
from . import forms


# Create your views here.
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Success')

    return render(request, 'forms_app/form_page.html', {'form': form})
