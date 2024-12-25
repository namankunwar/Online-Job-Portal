
from tkinter import N
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login
from .models import *
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from datetime import date
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    if  request.user.is_staff:
        return redirect("portal_1:admin_home")

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def elements(request):
    return render(request,"elements.html")



def job_listing(request):
    data= Job.objects.all()
    d={'data':data}

    return render(request,"job_listing.html",d)

def main(request):
    return render(request,"main.html")

def single_blog(request):
    return render(request,"single-blog.html")

def admin_home(request):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    return render(request,"admin_home.html")



def register(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        city = request.POST["city"]
        province = request.POST["province"]
        address = request.POST["address"]
        phone = request.POST["user_phone"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        img = request.FILES["user_image"]
        resume = request.FILES["user_cv"]

        try:
            user = User.objects.create_user(first_name=fname, last_name=lname, username = email, email=email, password=pwd )
            user.save()
            user_info = Candidate(
                user = user,
                gender= gender,
                city = city,
                province= province,
                address = address,
                phone = phone,
                image = img,
                cv =resume)
            user_info.save()
            messages.success(request,"You have been registerd. Please proceed to login")
        
        except IntegrityError:
            messages.error(request,"email already taken")
            return redirect("portal_1:register")

        
    return redirect("portal_1:login")
    
def signin_login(request):
    if  request.user.is_authenticated:
        return redirect("portal_1:index")
    if request.method == 'POST':
        username = request.POST['uemail']
        pwd = request.POST["password"]

        user = authenticate(username= username, password = pwd)

        if User.is_authenticated and user.is_staff ==True:
            login(request,user)
            return redirect("portal_1:admin_home")
            
        elif User.is_authenticated  :
            login(request,user)
            return redirect("portal_1:index")
        else:
            messages.error(request, "Bad credentials")
            return redirect("portal_1:login")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def user_profile(request):
     if not request.user.is_authenticated:
         return redirect("portal_1:login")
     candidate = Candidate.objects.get(user=request.user)
     if request.method=="POST":   
         email = request.POST['email']
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         phone = request.POST['phone']
         city = request.POST["city"]
         province = request.POST["province"]
         address = request.POST["address"]
         resume = request.FILES["user_cv"]
         candidate.user.email = email
         candidate.user.first_name = first_name
         candidate.user.last_name = last_name
         candidate.phone = phone
         candidate.address = address
         candidate.cv = resume
         candidate.city = city
         candidate.province = province
         candidate.save()
         candidate.user.save()
 
         try:
             image = request.FILES['user_image']
             candidate.image = image
             candidate.save()
             messages.success(request,"You have updated")
             return redirect("/")
         except:
             messages.success(request,"failed to updated")
        
         return render(request, "user_profile.html", )
     return render(request, "user_profile.html", {'candidate':candidate} )

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect("/")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

# def admin_login(request):
#      if request.method == 'POST':
#          username = request.POST['admin']
#          pwd = request.POST["password"]

#          user = authenticate(username= username, password = pwd)

#          if user.is_staff:
#              login(request,user)
#              return redirect("portal_1:admin_home")
#          else:
#              messages.error(request, "Bad credentials")
#              return redirect("portal_1:admin_login")
#      return render(request, 'admin_login.html')

def view_user(request):
    if not request.user.is_authenticated:
        return redirect("portal_1:login")
    data= Candidate.objects.all()
    d={'data':data}
    return render(request,"view_user.html",d)


def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    data= User.objects.get(id=pid)
    data.delete()
    return redirect("portal_1:view_user")

def add_job(request):
    if not request.user.is_authenticated:
        return redirect("portal_1:login")
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        image = request.FILES['image']
        company = request.POST['company']
        opening= request.POST['openings']
        try:
            job = Job.objects.create( title=title, 
                                    start_date=start_date, 
                                    end_date=end_date,
                                     n_openings=opening,
                                      salary=salary, 
                                      image=image,
                                       experience=experience,
                                        location=location,
                                         skills=skills,
                                          company=company, 
                                          descriptions=description,
                                           published_date=date.today())
            job.save()
            messages.success(request,"Jobs have been added")
        except:
            messages.error(request,"something wrong happened")
        
        return render(request, "add_job.html" )
    return render(request, "add_job.html")



def admin_joblist(request):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    data= Job.objects.all()
    d={'data':data}
    return render(request, "admin_joblist.html",d)

def delete_job(request,pid):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    data= Job.objects.get(id=pid)
    data.delete()
    return redirect("portal_1:view_user")

def edit_job(request, myid):
    if not request.user.is_authenticated:
        return redirect("portal_1:login")
    job = Job.objects.get(id=myid)
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        image = request.FILES['image']
        company = request.POST['company']
        opening= request.POST['openings']

        job.title = title
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.descriptions = description
        
        job.company=company
        job.n_openings=opening
        try:
            job.save()
            if start_date:
                job.start_date = start_date
                job.save()
            if end_date:
                job.end_date = end_date
                job.save()
            if image:
                job.image=image
                job.save()
                messages.success(request,"Jobs have been updated")
                return redirect("portal_1:admin_joblist")
        except:
             messages.success(request,"failed to updated")
        
        return render(request, "edit_job.html" )
    return render(request, "edit_job.html", {'job':job })



def search(request):
    title =""
    joblist = Job.objects.all()
    location =""
    if request.method=="POST":
        title = request.POST["key"]
        location = request.POST["location"]
        joblist = joblist.filter(Q(title__icontains=title) | Q(location__icontains=location))
    paginator = Paginator(joblist,1)
    pagen = request.GET.get('page')
    pageobj = paginator.get_page(pagen)
    return render(request, "job_list.html", {"data":pageobj.object_list,
                                                "key":title,
                                                "location":location,
                                                "page_obj":pageobj})


def job_detail(request,pid):
    element = Job.objects.get(id=pid)
   
    #checking whether job is aready applied or not
    if request.user.is_authenticated:
         user=request.user
         candidate = Candidate.objects.get(user=user)
         data= Jobapplicant.objects.filter(candidate=candidate)
         li=[]
         for i in data:
             li.append(i.job.id) #accessing id through job_id and all applied job id is stored in li

    else:
         return redirect("portal_1:login")
    
    return render(request,"job_detail.html",{ "job":element, "li":li})


def job_apply(request, pid):
    if not request.user.is_authenticated:
         return redirect("portal_1:login")
    
    user = request.user
    candidate= Candidate.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1= date.today()
    pending ="Pending"
    if job.end_date < date1:
         closed=True
         return render(request, "job_detail.html", {'closed':closed, 'job':job,})
    elif job.start_date > date1:
         notopen=True
         return render(request, "job_detail.html", {'notopen':notopen, 'job':job,})
    else:
        Jobapplicant.objects.create(job=job, candidate=candidate, company=job.company, status=pending, apply_date=date.today())
        alert=True
        return render(request, "index.html", {'job':job,'alert':alert})
        
        #return render(request, "job_detail.html", {'job':job,'alert':alert}) 


def admin_jobapplicant(request):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    data= Jobapplicant.objects.all()
    d={'data':data}
    return render(request, "admin_jobapplicant.html",d)

def delete_applicant(request,pid):
    if not request.user.is_staff:
        return redirect("portal_1:login")
    data= Jobapplicant.objects.get(id=pid)
    data.delete()
    return redirect("portal_1:admin_jobapplicant")

def applied_job(request,pid):
    if not request.user.is_authenticated:
        return redirect("portal_1:login")
    data= Jobapplicant.objects.filter(candidate=pid)

    d={'data':data}
    return render(request, "applied_job.html",d)
