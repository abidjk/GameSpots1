from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'home.html')

def Signup(request):
    return render(request, 'signup.html')

def Signin(request):
    return render(request, 'signin.html')

def masterFn(request):
    return render(request, 'usermaster.html')       


