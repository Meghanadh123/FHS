from django.http import HttpResponse
from django.shortcuts import redirect, render
def loginpage(request):
    return render(request,"login.html")
def aboutpage(request):
    return render(request,"about.html")
def contactpage(request):
    return render(request,"contact.html")
def indexpage(request):
    return render(request,"index.html")
def menupage(request):
    return render(request,"menu.html")
def hotelpage(request):
    return render(request,"Hotel.html")
def newsdetailpage(request):
    return render(request,"news-detail.html")
