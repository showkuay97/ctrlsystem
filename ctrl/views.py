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
    options =options_std.objects.all()
    pc = repair_cmpt.objects.all()
    slct =request.GET("select_class")


    return render(request,'pcstudent.html',{'pcs':pc,'ops':options,'select':slct})

def pcteacher(request):

    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')

def selection(request):
    slct =request.GET("select_class")
    # if request.method == 'POST':
    #     form = selection(request.POST)

    # if form.is_valid():
    #   slct = form.cleaned_data['value']
    return render(request,'pcstudent.html',{'select':slct})
 
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