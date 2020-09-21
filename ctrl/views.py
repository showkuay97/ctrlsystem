from django.http import request
from django.shortcuts import render
from django.urls.base import is_valid_path
from .models import cmpt_detail,options_std,options_tcher,repair_cmpt,report
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from .forms import opsForm,repiarForm,input_detail
# from .forms import create_repair


# Create your views here.
def index(request):
    comp = report.objects.all()
    return render(request,'index.html',{'comps':comp})

def Login(request):
    return render(request,'Login.html')

def pcstudent(request):
    pc = repair_cmpt.objects.all()
    f = opsForm()
    input = input_detail()
    form_repair = repiarForm()
    if request.method == 'POST':
        rq = input_detail(request.POST)
        req = opsForm(request.POST)
        if rq.is_valid():
            result = rq.cleaned_data['check_repair']
            print(result)
            return render(request,'pcstudent.html')
        if req.is_valid():
            res = req.cleaned_data['field']
            pc = repair_cmpt.objects.filter(class_room=res)
            print(res)
            return render(request,'pcstudent.html',{'pcs':pc,'select':res,'form':f,'F_repair':form_repair,'txt':input})
    return render(request,'pcstudent.html',{'form':f,'F_repair':form_repair,'txt':input})

def create_repair(request):
    
    if request.method == 'POST':
        pc_repair = request.POST.getlist('check_repair')
        divice_repair = request.POST.getlist('de_check_repair')
        other_repair = request.POST['other_repair']
        # if pc_repair=='' or '[]' and divice_repair == '' or '[]':
        #     post_err ="not found"
        #     return render(request,'pcstudent.html',{'err':post_err})
        # else :
        if pc_repair is '[]' :
            post_err ="not found"
            return render(request,'pcstudent.html',{'err':post_err})
        else:
            print(pc_repair)
            
        print(divice_repair)
        print(other_repair)
        # print(type(values))
        
        
    return render(request,'pcstudent.html')

def pcteacher(request):

    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')

def test(request):
    input = input_detail()
    
    return render(request,'testmodal.html',{'txt':input})


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