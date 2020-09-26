from django.http import request,HttpRequest
from django.shortcuts import render ,redirect
from django.urls.base import is_valid_path
from .models import cmpt_detail,options_std,options_tcher,repair_cmpt,report
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from .forms import opsForm,repiarForm,input_detail
from datetime import datetime
from django.contrib import messages
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
    form_repair = repiarForm()
    # for i in pc:
    #     print(i.id)
    if request.method == 'POST':
        rq = input_detail(request.POST)
        req = opsForm(request.POST)
        if rq.is_valid():
            result = rq.cleaned_data['check_repair']
            print(result)
            return render(request,'pcstudent.html')
        if req.is_valid():
            res = req.cleaned_data['field']
            pc = repair_cmpt.objects.filter(class_room=res).order_by('id')
            print(res)
            return render(request,'pcstudent.html',{
                'pcs':pc,
                'select':res,
                'form':f,
                'F_repair':form_repair})
    return render(request,'pcstudent.html',{'form':f,'F_repair':form_repair})

def create_repair(request,id):
    # messages.add_message(request,messages.success,'ส่งเรื่องแจ้งแล้ว')
    # messages.add_message(request,messages.error,'กรุณากรอกข้อมูลอาการของคอมพิวเตอร์')
    if request.method == 'POST':
        pc_repair = request.POST.getlist('check_repair')
        divice_repair = request.POST.getlist('de_check_repair')
        other_repair = request.POST['other_repair']
        # id_pc = request.POST['get_id_cmpt']
        # btn_id = request.POST['btnid']
        if pc_repair == [] and divice_repair == [] and other_repair.strip() =='':
            messages.error(request, 'กรุณาระบุอาการของคอมพิวเตอร์!')
            # return render(request,'repair.html',{'err':post_err})
            return redirect('/repair/%d'%id)
        else:
            # messages.success(request, 'Your password was updated successfully!')
            # print(id_pc)
            err_pc = ""
            for i in pc_repair:
                err_pc+=i+","
            
            for j in divice_repair:
                err_pc+=j+","
            err_pc+=other_repair
            print(err_pc)
            # print("btn "+btn_id)
            print("id = "+str(id))
            date_re = datetime.now()
            cmpt = repair_cmpt.objects.get(id=id)
            cmpt.detail_repair = err_pc
            cmpt.date_report = date_re.strftime("%d/%m/%Y  %H:%M:%S")
            # print(date_re.strftime("%d/%m/%Y"))
            cmpt.save()
            return redirect('/pcstudent/')
    return redirect('/pcstudent/')

def pcteacher(request):

    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')

def test(request):
    pc = options_std.objects.all()
    return render(request,'testmodal.html',{'pcs':pc})

def tester(request,id):
    if request.method == 'POST':
        res = request.POST['get_id_cmpt']
        print(res)
        print(id)

    return redirect('/test/')
    
def repair(request,id):
    ids = repair_cmpt.objects.get(id=id)
    print(id)
    return render(request,'repair.html',{'ids':ids,})

# def select(request):
#     if request.method=='POST':
#         results = request.POST['selections']
#         pc = repair_cmpt.objects.all()
#         return render(request,'pcstudent.html',{'result':str(results)})

# def testdata(request):
#     for i in range(201,209):
#         for j in range(1,52,1):
#             add_cmpt = repair_cmpt.objects.create(
#                 class_room = str(i),
#                 slug_repair = str(i),
#                 No_cmpt = str(j),
#                 img_cmpt = str('/static/assets/img/pc1.png'),
#                 stat_cmpt = str("ปกติ"),
#             )
#     add_cmpt.save()
#     return render(request,'index.html',{'ss':"Success"})