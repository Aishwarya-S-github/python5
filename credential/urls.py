from . import views
from django.urls import path
app_name='credential'



urlpatterns = [


    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('submit', views.submit, name='submit'),
    path('logout', views.logout, name='logout'),
    path('forms', views.forms, name='forms'),
]