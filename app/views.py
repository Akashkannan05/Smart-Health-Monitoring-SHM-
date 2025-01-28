from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
from .models import UserProfileModel,DoctorProfileModel

def Record(request,MedicalID=None):
    qs=UserProfileModel.objects.filter(MedicalID=MedicalID)
    if not qs.exists():
        Dictionary={"Record":False}
        return (request,'record.html',Dictionary)
    qs=UserProfileModel.objects.get(MedicalID=MedicalID)
    Name=qs.User.username
    DateOfBirth=qs.DateOfBirth
    Gender=qs.Gender
    Age=qs.Age
    PhoneNumber=qs.PhoneNumber
    Address=qs.Address
    ReportDate=qs.MedicalRecord.Date
    DoctorName=qs.MedicalRecord.Doctor.User.username
    Symptoms=qs.MedicalRecord.Symptoms
    Diagnosis=qs.MedicalRecord.Diagnosis
    TestsConducted=qs.MedicalRecord.TestsConducted
    TreatmentPlan=qs.MedicalRecord.TreatmentPlan
    AdditionalNotes=qs.MedicalRecord.AdditionalNotes

    Dictionary={"Record":True,"Name":Name,"DateOfBirth":DateOfBirth,"Gender":Gender,"Age":Age,"PhoneNumber":PhoneNumber,
                "Address":Address,"ReportDate":ReportDate,"DoctorName":DoctorName,"Symptoms":Symptoms,
                "Diagnosis":Diagnosis,"TestsConducted":TestsConducted,"TreatmentPlan":TreatmentPlan,
                "AdditionalNotes":AdditionalNotes}
    
    return render(request,'pagedownload.html',Dictionary)

def doctor_signup(request):
    if (request.method =="POST"):
        username=request.POST['Name']
        email=request.POST['E-mail']
        gender=request.POST['Gender']
        license_no=request.POST['license-no']
        Specialization=request.POST['Specilization']
        password=request.POST['password']
        ConformPassword=request.POST['ConformPassword']
        userqs=User.objects.filter(username=username)
        if userqs.exists():
            return render(request,'doctorlogin/index.html',{'name_error':True},status=403)
        if(password!=ConformPassword):
            return render(request,'doctorlogin/index.html',{'pass_error':True},status=406)
        userobj=User(username=username,email=email)
        userobj.set_password(password)
        userobj.save()
        doctor=DoctorProfileModel(User=userobj,gender=gender,LicenseNumber=license_no,Specialization=Specialization)
        doctor.save()
        print("User Added")
        user = authenticate(username=username, password=password)
        login(request,user)
        return render(request,'index.html',status=200)
    return render (request,"doctor_signup/index.html",status=200)

def doctor_login(request):
    if (request.method=="POST"):
        LicenseNumber=request.POST['License-no']
        password=request.POST['password']
        userqs=DoctorProfileModel.objects.filter(LicenseNumber=LicenseNumber)
        if not userqs.exists():
            return render(request,'doctorlogin/index.html',{'name_error':True},status=403)
        userqs=DoctorProfileModel.objects.get(LicenseNumber=LicenseNumber)
        doctor=userqs.User.username
        user = authenticate(request,username=doctor, password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html',status=200)
        # return render(request,'profile.html',status=200)
        return render(request,'doctorlogin/index.html',{'pass_error':True},status=403)
    return render(request,"doctorlogin/index.html")

def patient_login(request):
    if(request.method =="POST"):
        username=request.POST['username']
        password=request.POST['password']
        userqs=User.objects.filter(username=username)
        if not  userqs.exists():
            return render(request,'patientlogin/index.html',{'name_error':True},status=404)
        userqs=User.objects.get(username=username)
        print("pass=",password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html',status=200)
            
        return render(request,'patientlogin/index.html',{'pass_error':True},status=403)
    
    return render(request,"patientlogin/index.html")

def patient_signup(request):
    return render(request,'patientsignup/index.html')

def home(request):
    return render(request,'index.html',status=200)

def profile(request):
    return render(request,'profile.html')