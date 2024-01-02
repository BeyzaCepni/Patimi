from django.shortcuts import render
from django.http.response import HttpResponse
data = {    
    "ilanlar": [
        {
            "id": 1,
            "tur": "Tekir Kedi",
            "image": "tekir_kedi.jpg",
            "ilce": "Beşiktaş",
            "sehir": "İstanbul",
            "tarih": "28/10/2023",
            "is_active": True,
            "description": "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet lorem"
        },
        {
            "id": 3,
            "tur": "kopek",
            "image": "golden.jpg",
            "ilce": "merkez",
            "sehir": "Afyon",
            "tarih": "28/09/2023",
            "is_active": True,
            "description": "Erat ipsum justo amet duo et elitr dolor, est duo duo eos lorem sed diam stet diam sed stet lorem"
        }       
    ]
}    
# Create your views here.
def index(request):
    context = {
        "ilanlar": data["ilanlar"]
    }
    return render(request,"index.html", context)

def patimibuldun(request):
    context = {
        "ilanlar": data["ilanlar"]
    }
    return render(request,"PatimiBuldun.html", context)

def patimibakilacak(request):
    return render(request,"PatimiBakilacak.html")

def patimisahiplen(request):
    context = {
        "ilanlar": data["ilanlar"]
    }
    return render(request,"PatimiSahiplen.html", context)

def patimiyakinimda(request):
    return render(request,"PatimiYakinimda.html")

def iletisim(request):
    return render(request,"contact.html")

def hakkimizda(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def loginPage(request):
    return render(request,"loginPage.html")

def profil(request):
    return render(request,"profil.html")

def profilEdit(request):
    return render(request,"profilEdit.html")

def ilanDetails(request,id):
    return render(request,"ilan_details.html")



