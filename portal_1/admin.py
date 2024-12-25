from django.contrib import admin
from .models import *
from  django.contrib.auth.models  import  Group  # new
#...
admin.site.unregister(Group)

# Register your models here.

admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Jobapplicant)