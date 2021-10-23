
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from patelbill.models import *
from django.contrib.auth.models import User

def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('Mainn')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)
def LOGOUT(request):
    logout(request)
    return redirect('Login')
def Signup(request):
    error = False
    error2 = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        c = d['cpwd']
        f = d['fname']
        l = d['lname']
        e = d['em']
        user = User.objects.filter(username=u)
        if user:
            error2 = True
        elif c!=p:
            error = True
        else:
             User.objects.create_user(username=u, password=p,email= e,first_name =f,last_name =l)
             return redirect('Login')
    dd = {'error':error,'error2':error2}
    return render(request, "signup.html",dd)
def Forgot(request):
    error = False
    form = False
    udata = False
    if request.method == "POST":
        dd = request.POST
        name = dd["form"]
        if name == "submit email":
            e = dd['em']
            user = User.objects.filter(email = e)
            if user:
                form = True
                udata = user[0]
            else:
                error = True
        if name == 'submit pwd':
            p = dd ['pwd']
            c = dd ['cpwd']
            u = dd ['idd']
            user = User.objects.get(id=u)
            user.set_password(p)
            user.save()
            return redirect ('Login')
    d = {"form":form,"error":error,"udata":udata}
    return render(request,'forgot.html',d)
def Home (request):
    if request.method == "POST":
        MMB = request.POST['totalbill']
        MMU = request.POST['totalunit']
        SMB = request.POST['meter21']
        SMU = request.POST['meter2']
        I = request.POST['img']
        D = request.POST['date']
        a = float(MMB) / float(MMU)
        b = float(SMU) - float(SMB)
        c = a * b
        u = int(MMU) - b
        r = int(MMB) - c
        Calculator.objects.create(Main_meter_bill_RS =MMB, Main_Meter_Unit =MMU,Per_Unit_Rs = a,Second_Meter_Unit =b,First_Meter_Unit= u,First_meter_bill_RS = r,Second_meter_bill_RS = c,Bill_image =I,Bill_date = D)
        return redirect('Mainn')

    return render(request,'billcalculator.html')


def Main(request):

    bill = Calculator.objects.all().order_by('-Bill_date')
    d= {"bill":bill}
    return render(request, 'index.html',d)

def delete_blog(request, pid):
    data = Calculator.objects.get(id=pid)
    data.delete()
    return redirect('Mainn')