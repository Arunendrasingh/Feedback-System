from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('login', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('showfeedback/', views.showfeedback, name='showfeedback'),
    path('save_feedback', views.save_feedback, name='save_feedback'),
    path('Comming_Soon', views.comming_soon, name='Comming Soon'),
]