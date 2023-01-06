from . import views
from django.urls import path
app_name='bankingapp'
urlpatterns = [
    path('',views.demo,name='demo'),

]
