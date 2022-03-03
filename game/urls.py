from django.urls import path
from .import views

urlpatterns=[

    path('',views.Home, name="home"),
    path('signup',views.Signup, name="sign"),
    path('signin',views.Signin, name="signin"),
    path('usermaster',views.masterFn, name="usermaster")
]