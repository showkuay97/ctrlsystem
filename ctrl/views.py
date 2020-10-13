from django.http import request,HttpRequest
from django.shortcuts import render ,redirect
from django.urls.base import is_valid_path
from .models import cmpt_detail,options_std,options_tcher,repair_cmpt,report
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from .forms import opsForm,repiarForm,input_detail,adminsForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import create_repair


# Create your views here.
@login_required(login_url='/')
def index(request):
    
    return render(request,'index.html',{})

def Login(request):

    return render(request,'Login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user =  auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('index')
    else:
        messages.error(request, 'ไม่พบผู้ใช้งานนี้!')
        return redirect('Login')

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('Login')

@login_required(login_url='/')
def pcstudent(request):
    pc = repair_cmpt.objects.all()
    f = opsForm()

    if request.method == 'POST':
        # rq = input_detail(request.POST)
        req = opsForm(request.POST)
        # if rq.is_valid():
        #     result = rq.cleaned_data['check_repair']
        #     print(result)
        #     return redirect('/pcstudent/')
        if req.is_valid():
            res = req.cleaned_data['field']
            pc = repair_cmpt.objects.filter(class_room=res).order_by('id')
            print(res)
            return render(request,'pcstudent.html',{
                'pcs':pc,
                'select':res,
                'form':f,
            })
    return render(request,'pcstudent.html',{'form':f})
@login_required(login_url='/')
def create_repair(request,id):
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
            if other_repair.strip() != ' ':
                err_pc+=other_repair
            print(err_pc)
            # print("btn "+btn_id)
            print("id = "+str(id))
            date_re = datetime.now()
            cmpt = repair_cmpt.objects.get(id=id)
            cmpt.detail_repair = err_pc
            cmpt.user_report = request.user.username
            cmpt.stat_cmpt ='กำลังดำเนินการ'
            cmpt.date_report = date_re.strftime("%d/%m/%Y  %H:%M:%S")
            # print(date_re.strftime("%d/%m/%Y"))
            cmpt.save()
            return redirect('/pcstudent/')
    return redirect('/pcstudent/')
@login_required(login_url='/')
def create_repairaj(request,id):
    if request.method == 'POST':
        pc_repair = request.POST.getlist('check_repair')
        divice_repair = request.POST.getlist('de_check_repair')
        other_repair = request.POST['other_repair']
        # id_pc = request.POST['get_id_cmpt']
        # btn_id = request.POST['btnid']
        if pc_repair == [] and divice_repair == [] and other_repair.strip() =='':
            messages.error(request, 'กรุณาระบุอาการของคอมพิวเตอร์!')
            # return render(request,'repair.html',{'err':post_err})
            return redirect('/repairaj/%d'%id)
        else:
            # messages.success(request, 'Your password was updated successfully!')
            # print(id_pc)
            err_pc = ""
            for i in pc_repair:
                err_pc+=i+","
            
            for j in divice_repair:
                err_pc+=j+","
            if other_repair.strip() != ' ':
                err_pc+=other_repair
            print(err_pc)
            # print("btn "+btn_id)
            print("id = "+str(id))
            date_re = datetime.now()
            cmpt = repair_cmpt.objects.get(id=id)
            cmpt.detail_repair = err_pc
            cmpt.user_report = request.user.username
            cmpt.stat_cmpt ='กำลังดำเนินการ'
            cmpt.date_report = date_re.strftime("%d/%m/%Y  %H:%M:%S")
            # print(date_re.strftime("%d/%m/%Y"))
            cmpt.save()
            return redirect('/pcteacher/')
    return redirect('/pcteacher/')
@login_required(login_url='/')
def pcteacher(request):
    pc = repair_cmpt.objects.all()
    f = repiarForm(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            res = f.cleaned_data['field']
            pc = repair_cmpt.objects.filter(class_room=res).order_by('id')
            print(res)
            return render(request,'pcteacher.html',{
                'pcs':pc,
                'select':res,
                'form':f,
            })
    return render(request,'pcteacher.html',{'form':f,})

# def register(request):
#     return render(request,'regis.html')

# def Dashboard(request):
#     return render(request,'Dashboard.html')

@login_required(login_url='/') 
def admins(request):
    pc = repair_cmpt.objects.all()
    pc = repair_cmpt.objects.filter(stat_cmpt='กำลังดำเนินการ').order_by('date_report')
    return render(request,'admin.html',{'pcs':pc,})

def test(request):
    pc = options_std.objects.all()
    return render(request,'testmodal.html',{'pcs':pc})

def tester(request,id):
    if request.method == 'POST':
        res = request.POST['get_id_cmpt']
        print(res)
        print(id)

    return redirect('/test/')

@login_required(login_url='/')
def repair(request,id):
    ids = repair_cmpt.objects.get(id=id)
    print(id)
    return render(request,'repair.html',{'ids':ids,})

@login_required(login_url='/')
def repairaj(request,id):
    ids = repair_cmpt.objects.get(id=id)
    print(id)
    return render(request,'repairaj.html',{'ids':ids,}) 

@login_required(login_url='/')
def receive(request,id):
    ids = repair_cmpt.objects.get(id=id)
    print(id)
    return render(request,'receive.html',{'ids':ids,})

@login_required(login_url='/')
def pcreceive(request,id):
    if request.method == 'POST':
        pc_repair = request.POST.getlist('check_repair')
        divice_repair = request.POST.getlist('de_check_repair')
        other_repair = request.POST['other_repair']
        # id_pc = request.POST['get_id_cmpt']
        # btn_id = request.POST['btnid']
        if pc_repair == [] and divice_repair == [] and other_repair.strip() =='':
            messages.error(request, 'กรุณาระบุอาการของคอมพิวเตอร์!')
            # return render(request,'repair.html',{'err':post_err})
            return redirect('/receive/%d'%id)
        else:
            # messages.success(request, 'Your password was updated successfully!')
            # print(id_pc)
            err_pc = ""
            for i in pc_repair:
                err_pc+=i+","
            
            for j in divice_repair:
                err_pc+=j+","
            if other_repair.strip() != ' ':
                err_pc+=other_repair
            print(err_pc)
            # print("btn "+btn_id)
            print("id = "+str(id))
            date_re = datetime.now()
            cmpt = repair_cmpt.objects.get(id=id)
            cmpt.check_repair = err_pc
            cmpt.date_input = date_re.strftime("%d/%m/%Y  %H:%M:%S")
            # print(date_re.strftime("%d/%m/%Y"))
            cmpt.save()
            return redirect('/admins/')
    return redirect('/admins/')

@login_required(login_url='/')
def send(request,id):
    ids = repair_cmpt.objects.get(id=id)
    print(id)
    return render(request,'send.html',{'ids':ids,})

@login_required(login_url='/')
def sendpc(request,id):
    if request.method == 'POST':
        pc_repair = request.POST.getlist('check_repair')
        divice_repair = request.POST.getlist('de_check_repair')
        other_repair = request.POST['other_repair']
        # id_pc = request.POST['get_id_cmpt']
        # btn_id = request.POST['btnid']
        if pc_repair == [] and divice_repair == [] and other_repair.strip() =='':
            messages.error(request, 'กรุณาระบุอาการของคอมพิวเตอร์!')
            # return render(request,'repair.html',{'err':post_err})
            return redirect('/send/%d'%id)
        else:
            err_pc = ""
            for i in pc_repair:
                err_pc+=i+","
            
            for j in divice_repair:
                err_pc+=j+","
            if other_repair.strip() != ' ':
                err_pc+=other_repair
            print(err_pc)
            # print("btn "+btn_id)
            print("id = "+str(id))

            reportdata = cmpt_detail.objects.get(id=id)
            for item in pc_repair:
                if item =="ลง Windows ใหม่":
                    reportdata.count_windows +=1
                elif item == "เปลี่ยน Ram ใหม่":
                    reportdata.count_ram +=1
                elif item == "เปลี่ยน PSUใหม่":
                    reportdata.count_psu +=1
                # elif item == "เปลี่ยน Board ใหม่":
                    # reportdata.count_windows +=1
                elif item == "เปลี่ยน Garphic Card ใหม่":
                    reportdata.count_gpu +=1
                elif item == "เปลี่ยน HDD ใหม่":
                    reportdata.count_hdd +=1
                elif item == "เปลี่ยน SSD ใหม่":
                    reportdata.count_ssd +=1
                elif item == "เปลี่ยนสาย Sata ใหม่":
                    reportdata.count_power +=1
                elif item == "เปลี่ยนสาย PSU ใหม่":
                    reportdata.count_power +=1
                elif item == "เปลี่ยน Adaptor ใหม่":
                    reportdata.count_windows +=1
                elif item == "เปลี่ยนสายจอใหม่":
                    reportdata.count_power +=1
                elif item == "ลง License ใหม่":
                    reportdata.count_lic +=1
                elif item == "ลง Program ใหม่":
                    reportdata.count_program +=1
                elif item == "เข้าหัว Lan ใหม่":
                    reportdata.count_internet +=1
                elif item == "เปลี่ยนคีย์บอร์ดใหม่":
                    reportdata.count_keyboard +=1
                elif item == "เปลี่ยนเมาส์ใหม่":
                    reportdata.count_mouse +=1

            date_re = datetime.now()
            cmpt = repair_cmpt.objects.get(id=id)
            cmpt.repair = err_pc
            cmpt.stat_cmpt='ปกติ'
            cmpt.detail_repair = ''
            cmpt.date_report =''
            cmpt.date_input=''
            cmpt.check_repair =''
            cmpt.user_report = ''
            cmpt.date_output = date_re.strftime("%d/%m/%Y  %H:%M:%S")
            # print(date_re.strftime("%d/%m/%Y"))
            cmpt.save()
            reportdata.count_all+=1;
            reportdata.save()
            return redirect('/admins/')
    return redirect('/admins/')

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
#                 No_cmpt = str(j)
#             )
#     add_cmpt.save()
#     return render(request,'index.html',{'ss':"Success"})