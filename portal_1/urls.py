
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path, reverse
from . import views

app_name = "portal_1"
urlpatterns = [
   # path("",lambda request:render(request,"index.html"), name="index"),
    path("",views.index, name="index"),
    path ('index/', lambda request:redirect("/") ),
    path('about',lambda request:render(request,'about.html'),name='about'),
    path('blog',lambda request:render(request,'blog.html'),name='blog'),
    path('contact',lambda request:render(request,'contact.html'),name='contact'),
    path('elements',lambda request:render(request,'elements.html'),name='elements'),
  #  path('index',lambda request:redirect("portal_1:index"),name="index2"),
   
    path('login',lambda request:render(request,'login.html'),name='login'),
    path('main',lambda request:render(request,'main.html'),name='main'),
    path('register',lambda request:render(request,'register.html'),name='register'),
    path('single-blog',lambda request:render(request,'single-blog.html'),name='single-blog'),
    path("do_register", views.register, name="do_register"),
    path('signin', views.signin_login, name='signin'),
    path('logout', views.logout, name='logout'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('change_password', views.change_password, name='change_password'),
   # path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('view_user', views.view_user, name='view_user'),
    path('delete_user <int:pid>', views.delete_user, name='delete_user'),
    path('add_job', views.add_job, name='add_job'),
    path('admin_joblist', views.admin_joblist, name='admin_joblist'),
    path('delete_job <int:pid>', views.delete_job, name='delete_job'),
    path("edit_job <int:myid>/", views.edit_job, name="edit_job"),  
     path('job_listing',views.job_listing,name ="job_listing"),
     path('job_list',views.search,name ="job_list"),
     path('job_detail <int:pid>',views.job_detail,name="job_detail"),
     path('job_apply <int:pid>', views.job_apply, name='job_apply'),  
     path('admin_jobapplicant', views.admin_jobapplicant, name='admin_jobapplicant'), 
     path('delete_applicant <int:pid>', views.delete_applicant, name='delete_applicant'),
    path('applied_job <int:pid>', views.applied_job, name='applied_job'),
]

