from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'Login.html')

def pcstudent(request):
    return render(request,'pcstudent.html')

def pcteacher(request):
    return render(request,'pcteacher.html')

def register(request):
    return render(request,'regis.html')

def Dashboard(request):
    return render(request,'Dashboard.html')
    
def admins(request):
    return render(request,'admin.html')