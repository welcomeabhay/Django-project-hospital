from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User,Group
from .forms import *

# Create your views here.

# for current user
def Current_user(request):
    status=''
    query_set = Doctor.objects.values_list('user',flat=True)
    p_set = Patient.objects.values_list('user',flat=True)
    user = request.user.id
    if user in query_set:
        print("user is doctor")
        status = 'doctor'
    elif user in p_set:
        print("user is patient")
        status = 'patient'
    else:
        status = 'none'

    print('group',query_set)
    return status

# function for home page.
def Home(request):
    user = Current_user(request)
    print('user',user)
    return render(request,'home.html',{'d':user})

# function for showing departments.
def Departments(request):
    depart = Department.objects.all()
    return render(request,'departments.html',{'dep':depart})

# function for showing doctor's list.
def Our_doctors(request):
    doctors = Doctor.objects.all()

    return render(request,'doctors.html',{'doc':doctors})

# function for  login.
def Login(request):
    if request.method=='POST':
        Fname=request.POST.get('uname')
        Psd=request.POST.get('psd')
        log_user=auth.authenticate(username=Fname,password=Psd)
        if log_user is not None:
            auth.login(request,log_user)
            return redirect("/")

        else:
            messages.info(request,"Incorrect username or password")
            return redirect("login")
    return render(request,"login.html")

# function for logout.
def Logout(request):
    auth.logout(request)
    return redirect("/")

# function for doctor's registration.
def Register(request):
    f = Doctor_form(request.POST or None)
    if request.method == 'POST':
        name=request.POST['name']
        det = request.POST['department']
        spec = request.POST['Specialization']
        Psd = request.POST['psd']
        Cpsd = request.POST['cpsd']

        if User.objects.filter(username=name,password=Psd).exists():
            messages.info(request,"already exist!")
        else:
            user = User.objects.create_user(username=name,password=Psd)
            user.save()
            group = Group.objects.get(name='Doctors')
            user.groups.add(group)
            dept = Department.objects.get(id=det)
            f = Doctor(user=user,name=name,Specialization=spec,department=dept)
            f.save()

            return redirect('login')
    return render(request,"register.html",{'form':f})


# function for patient's registration.
def Patient_reg(request):
    p = Patient_form(request.POST or None)
    if request.method == 'POST':
        Name=request.POST['name']
        Age = request.POST['age']
        Address = request.POST['address']
        Mobile = request.POST['mobile']
        Psd = request.POST['psd']
        Cpsd = request.POST['cpsd']

        if User.objects.filter(username=Name,password=Psd).exists():
            messages.info(request,"already exist!")
        else:
            user = User.objects.create_user(username=Name,password=Psd)
            user.save()
            group = Group.objects.get(name='Patients')
            user.groups.add(group)
            p = Patient(user=user,name=Name,age=Age,address=Address,mobile=Mobile)
            p.save()
            pr = Patient_Records(patient=p,diagnostics='',observations ='',treatments='')
            pr.save()

            return redirect('login')
    return render(request,"patient_reg.html",{'form':p})

# function for doctor's profile and edit.
def Edit_Doc(request):
    a = Doctor.objects.get(user=request.user.id)
    b = Doctor_profile(request.POST or None, request.FILES or None, instance=a)
    if request.method == "POST":
        if b.is_valid():
            b.save()
            return redirect("/")
        else:
            print("form is not valid")
    else:
        print("the method is not post")

    return render(request, "doc_profile.html", {"f": b})

# function for patient's data table(doctor's use only).
def Patient_data(request):
    data = Patient.objects.all()

    return render(request,'patient_data.html',{'pat':data})

# function for patient profile and edit (only for patient).
def Edit_pat(request):
    a = Patient.objects.get(user=request.user.id)
    b = Patient_profile(request.POST or None, request.FILES or None, instance=a)
    if request.method == "POST":
        if b.is_valid():
            b.save()
            return redirect("/")
        else:
            print("form is not valid")
    else:
        print("the method is not post")

    return render(request, "patient_profile.html", {"f": b})

# function for patient_record update (for doctor's use.).
def Patient_record(request,p_id):
    a = Patient_Records.objects.get(patient=p_id)
    b = Pat_record_form(request.POST or None, request.FILES or None, instance=a)
    if request.method == "POST":
        if b.is_valid():
            b.save()
            return redirect("/")
        else:
            print("form is not valid")
    else:
        print("the method is not post")

    return render(request, "patient_records.html", {"f": b,'p':a})
