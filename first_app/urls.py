from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', view=views.index, name='index')
]