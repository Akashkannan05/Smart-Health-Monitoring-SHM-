from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('profile',views.profile,name="profile"),
    path("record/<str:MedicalID>/",views.Record,name="Medical Record"),
    path('doctor/signup',views.doctor_signup,name="signup for doctor"),
    path('doctor/login',views.doctor_login,name='Login for doctor'),
    path('patient/login',views.patient_login,name='Patient login'),
    path('patient/signup',views.patient_signup)
]