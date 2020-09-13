from django.http import request
from django.shortcuts import render
from .models import cmpt_detail
from .models import repair_cmpt
from .models import report
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    comp = report.objects.all()
    return render(request,'index.html',{'comps':comp})

def Login(request):
    return render(request,'Login.html')

def pcstudent(request):
    pc = repair_cmpt.objects.all()
    return render(request,'pcstudent.html',{'pcs':pc})

def pcteacher(request):

    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')
 
# def testdata(request):
#     for i in range(201,209):
#         for j in range(1,51,1):
#             add_cmpt = repair_cmpt.objects.create(
#                 class_room = str(i),
#                 slug_repair = str(i),
#                 No_cmpt = str(j),
#                 img_cmpt = str('/static/img/pc1.png'),
#                 stat_cmpt = str("ปกติ"),
#             )
#     add_cmpt.save()
#     return render(request,'index.html',{'ss':"Success"})