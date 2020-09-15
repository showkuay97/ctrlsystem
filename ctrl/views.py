from django.http import request
from django.shortcuts import render
from .models import cmpt_detail,options_std,options_tcher,repair_cmpt,report
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def index(request):
    comp = report.objects.all()
    return render(request,'index.html',{'comps':comp})

def Login(request):
    return render(request,'Login.html')

def pcstudent(request):
    # pc = repair_cmpt.objects.filter(class_room=201)

    options =options_std.objects.all()
    if request.method == 'POST':
        res = request.POST['selections']
        pc = repair_cmpt.objects.filter(class_room=res)
        print(res)
        return render(request,'pcstudent.html',{'pcs':pc,'select':res,'ops':options})
    
    return render(request,'pcstudent.html')

def r201(request):
    pc = repair_cmpt.objects.filter(class_room=201)
    return render(request,'r201.html',{'pcs':pc})

def r202(request):
    pc = repair_cmpt.objects.filter(class_room=202)
    return render(request,'r201.html',{'pcs':pc})

def r203(request):
    return render(request,'r201.html',{'pcs':pc})

def pcteacher(request):

    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')

# def select(request):
#     if request.method=='POST':
#         results = request.POST['selections']
#         pc = repair_cmpt.objects.all()
#         return render(request,'pcstudent.html',{'result':str(results)})

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