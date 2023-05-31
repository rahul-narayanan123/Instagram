from django.urls import path
from instaapp import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('home', views.home,name='home'),
    path('myprofile',views.myprofile,name="myprofile"),
    path('logout',views.logout,name="logout"),
    path('edit',views.editprofile,name="edit"),
    path('addpost',views.addpost,name="addpost"),
    path('profileadds/<int:id>',views.profileadds,name="profileadds"),

   
    path('editpost/<int:id>',views.editpost,name="editpost"),


    path('deletepost/<int:a>/',views.deletepost,name="deletepost"),
    path('search',views.search,name="search"),
    path('comment/<int:id>',views.viewpage,name="comment"),
    path('searchprofile/<int:id>',views.searchprofile,name="searchprofile"),
















    


]