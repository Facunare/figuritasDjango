from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('figuritas/', views.figurita, name='figuritas'),
    path('signout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('verFigus/', views.verFigus, name='verFigus'),
    path('verFigus/<str:figu>/delete', views.delete_figus, name='figus_delete'),
    

]
