from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.form_name_view, name='form_name')
]