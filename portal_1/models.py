from pyexpat import model
from unicodedata import category
from urllib.robotparser import RobotFileParser
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Job(models.Model):
    title= models.CharField(max_length=100, null=True)
    descriptions= models.TextField()
    company= models.CharField(max_length=100, null=True)
    salary= models.IntegerField()
    n_openings= models.IntegerField()
    image= models.FileField(null=True)
    location=models.CharField(max_length=200,null=True)
    skills= models.CharField(max_length=200,null=True)
    experience = models.CharField(max_length=200, null=True)
    published_date = models.DateTimeField(null=True)
    end_date=models.DateField(null=True)
    start_date=models.DateField(null=True)
    category = models.CharField(max_length=100, null=True)
    
     
    def __str__(self):
        return self.title +" "+ self.company

class Candidate(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    phone= models.IntegerField()
    address=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    province =models.CharField(max_length=100)
    image= models.FileField(null=True)
    gender= models.CharField(max_length=100)
    cv = models.FileField()
    
     
    def __str__(self):
        return self.user.username

class Jobapplicant(models.Model):
    job= models.ForeignKey(Job, null=True, on_delete= models.CASCADE)
    candidate= models.ForeignKey(Candidate, null=True, on_delete= models.CASCADE)
    company = models.CharField(max_length=100, null=True)
    apply_date = models.DateField(null=True)
    status = models.CharField(max_length =100,  null=True)


    def _str_ (self):
        return self.job_id +" "+ self.candidate


   