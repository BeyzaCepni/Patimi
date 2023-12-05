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
    path("index",views.index),
    path("patimibuldun",views.patimibuldun),
    path("patimisahiplen",views.patimisahiplen),
    path("patimibakilacak",views.patimibakilacak),
    path("patimiyakinimda",views.patimiyakinimda),
    path("iletisim",views.iletisim),
    path("hakkimizda",views.hakkimizda),
    path("blog",views.blog),
 ]
 