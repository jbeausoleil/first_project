from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict_insert = {'my_insert': 'Welcome to my first application'}
    return render(request, '../templates/first_app/index.html', my_dict_insert)