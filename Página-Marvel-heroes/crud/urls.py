from django.urls import path

from . import views

urlpatterns = [
    path('',views.menu, name='menu'),
    path('index/',views.index, name='index'),
    path('detalle/<id_marvel>/',views.vista_detalle,name='detallemarvel'),
]