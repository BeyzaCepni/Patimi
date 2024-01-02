from django.urls import path, include
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
    path("",views.index, name="homepage"),
    path("index.html",views.index),
    path("PatimiBuldun.html",views.patimibuldun, name= "patimibuldun"),
    path("PatimiSahiplen.html",views.patimisahiplen, name= "patimisahiplen"),
    path("PatimiBakilacak.html",views.patimibakilacak, name="patimibakilacak"),
    path("PatimiYakinimda.html",views.patimiyakinimda, name= "patimiyakinimda"),
    path("contact.html",views.iletisim, name= "iletisim"),
    path("about.html",views.hakkimizda, name= "hakkimizda"),
    path("blog.html",views.blog, name="patimikonusalim"),
    path("loginPage.html",views.loginPage, name= "loginpage"),
    path("profil.html",views.profil, name= "profil"),
    path("profilEdit.html",views.profilEdit, name= "profiledit"),
    path("ilandetail/<int:id>",views.ilanDetails, name= "ilandetails"),
    path('social-auth/', include('social_django.urls', namespace='social')),

 ]
 