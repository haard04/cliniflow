from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('sp',views.sp,name='sp'),
    path('ca',views.ca,name='ca'),
    path('sp/doc', views.doctor_speech, name='doctor_speech'),
    path('sp/staff/', views.staff_speech, name='staff_speech'),
    path('ca/doc', views.doctor_custom, name='doctor_custom'),
    path('ca/staff/', views.staff_custom, name='staff_custom'),


]