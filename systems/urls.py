"""systems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from ctrl import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index"),
    path('',views.Login,name="Login"),  
    path('pcstudent/',views.pcstudent,name="pcstudent"),
    path('pcteacher/',views.pcteacher,name="pcteacher"),
    # path('register/',views.register),
    # path('Dashboard/',views.Dashboard),
    path('admins/',views.admins,name="admins"),
    path('create_repair/<int:id>',views.create_repair,name="create_repair"),
    path('create_repairaj/<int:id>',views.create_repairaj,name="create_repairaj"),
    path('pcreceive/<int:id>',views.pcreceive,name="pcreceive"),
    path('sendpc/<int:id>',views.sendpc,name="sendpc"),
    path('login/',views.login),
    path('logout/',views.logout),
    # path('tester/<int:id>',views.tester,name="tester"),asdasd
    path('repair/<int:id>',views.repair,name="repair"),
    path('repairaj/<int:id>',views.repairaj,name="repairaj"),
    path('receive/<int:id>',views.receive,name="receive"),
    path('send/<int:id>',views.send,name="send"),






    # path('pcstudent/select',views.select),
    
    # path('index/testdata',views.testdata),
]