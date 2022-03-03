from django.shortcuts import render

# Create your views here.


def Form(request):
    return render(request,'form.html')