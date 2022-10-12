from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('result/<result_id>',views.result, name='result'),
]