from django.urls import path
from .import views

urlpatterns=[

    path('',views.Home),
    path('signup',views.Signup, name="sign"),
    path('signin',views.Signin, name="signin"),
]