from django.conf.urls import url
from . import views

app_name = 'sudoku_app'

urlpatterns = [
    url('', views.index, name='app_index'),
]
