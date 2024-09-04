from django.shortcuts import render

# Create your views here.

def staticapp2(request):
    return render(request,'staticapp2.html')