from . import views
from django.urls import path

app_name = 'news'
urlpatterns = [
    path('', views.countryDashboard, name='newsHome'),
    path('countryDashboard/', views.countryDashboard, name='countryDashboard'),
    #path('<cinfo>/', views.countryDetail, name='countryDetail')
    path('<code>/', views.countryDetail, name='countryDetail')
]