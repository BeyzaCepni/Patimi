from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def patimibuldun(request):
    return render(request,"PatimiBuldun.html")

def patimibakilacak(request):
    return render(request,"PatimiBakilacak.html")

def patimisahiplen(request):
    return render(request,"PatimiSahiplen.html")

def patimiyakinimda(request):
    return render(request,"PatimiYakinimda.html")

def iletisim(request):
    return render(request,"contact.html")

def hakkimizda(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")



