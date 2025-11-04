from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('eventos/', views.eventos, name='eventos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('tienda-online/', views.tienda_online, name='tienda_online'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
]
