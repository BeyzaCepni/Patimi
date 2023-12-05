from django.urls import path
from. import views



#http://127.0.0.1:8000/ => index
#http://127.0.0.1:8000/index => index
#http://127.0.0.1:8000/patimibuldun => patimibuldun
#http://127.0.0.1:8000/patimisahiplen => patimisahiplen
#http://127.0.0.1:8000/patimibakilacak => patimibakilacak
#http://127.0.0.1:8000/patimiyakinimda => patimiyakinimda
#http://127.0.0.1:8000/iletisim => iletisim
#http://127.0.0.1:8000/hakkimizda => hakkimizda
#http://127.0.0.1:8000/blog => blog
 
urlpatterns = [
    path("",views.index),
    path("index.html",views.index),
    path("PatimiBuldun.html",views.patimibuldun),
    path("PatimiSahiplen.html",views.patimisahiplen),
    path("PatimiBakilacak.html",views.patimibakilacak),
    path("PatimiYakinimda.html",views.patimiyakinimda),
    path("contact.html",views.iletisim),
    path("about.html",views.hakkimizda),
    path("blog.html",views.blog),
 ]
 