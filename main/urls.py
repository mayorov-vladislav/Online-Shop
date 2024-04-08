from django.conf.urls import handler404, handler500
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')

]

handler404 = views.custom_404
handler500 = views.custom_500