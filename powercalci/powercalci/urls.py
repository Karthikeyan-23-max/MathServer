from django.contrib import admin 
from django.urls import path 
from powerapk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.power_calculator, name='power_calculator'),
]