from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import FacultyDetails
from .models import HODDetails
from .models import AdminDetails
from .models import User
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.hashers import make_password

def base(request):
    return render(request, 'base.html')

def login_f(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        faculty = authenticate(username=username,password=password)
        if faculty is None:
            return render(request,'login.html', {'error':'wrong username, password'})
        else:
            login(request,faculty)
            return redirect('home')
    return render(request,"login.html")

def login_hod(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        teacher = authenticate(username=username,password=password)
        if teacher is None:
            return render(request,'login.html', {'error':'wrong username, password'})
        else:
            login(request,teacher)
            return render(request,'hodhome.html')
    return render(request,"login.html")

def adminlogin(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        adminn = authenticate(username=username,password=password)
        if adminn is None:
            return render(request,'login.html', {'error':'wrong username, password'})
        else:
            login(request,adminn)
            return render(request,'AdminHome.html')
    return render(request,"login.html")


def logout(request):
    return redirect('base')
    
@login_required
def adminnhome(request):
    return render(request,"AdminHome.html")
   

@login_required  
def hod_home(request):
    if request.method == 'POST':
        teacher = request.user
        teacher_profile = HODDetails.objects.get(HOD=teacher)
        teacher_subject = teacher_profile.subject
        data = request.POST
        return redirect('hod.html')
    else:
        faculty = FacultyDetails.objects.all().order_by('faculty')
        return render(request,'hodhome.html', {'faculty':faculty})
    

def home(request):
    user = request.user
    faculty_id = user.id
    #username=form.cleaned_data.get('username')
    faculty_object = User.objects.get(id=faculty_id)
    faculty_details = FacultyDetails.objects.get(user=faculty_object)
    return render(request,'home.html',{'faculty':faculty_details})
    
@login_required(login_url='s_manage:login')
def logout_view(request):
    logout(request)
    return redirect('myaccounts:home')


# @login_required    
# def term1(request):
#     student = request.user
#     student_id = student.id
#     student_object = User.objects.get(id=student_id)
#     student_details = StudentDetails.objects.get(user=student_object)
#     term1_marks = Term1.objects.get(user=student_details)
#     return render(request, 'marks.html', {'marks':term1_marks})
# @login_required
# def term2(request):
#     student = request.user
#     student_id = student.id
#     student_object = User.objects.get(id=student_id)
#     student_details = StudentDetails.objects.get(user=student_object)
#     term2_marks = Term2.objects.get(user=student_details)
#     return render(request, 'marks.html', {'marks':term2_marks})
# @login_required
# def finals(request):
#     student = request.user
#     student_id = student.id
#     student_object = User.objects.get(id=student_id)
#     student_details = StudentDetails.objects.get(user=student_object)
#     finals_marks = Finals.objects.get(user=student_details)
#     return render(request, 'marks.html', {'marks':finals_marks})

# @login_required
# def reportcard(request):
#     student = request.user
#     student_id = student.id
#     student_object = User.objects.get(id=student_id)
#     student_details = StudentDetails.objects.get(user=student_object)
#     term1_marks = Term1.objects.get(user=student_details)
#     term2_marks = Term2.objects.get(user=student_details)
#     finals_marks = Finals.objects.get(user=student_details)
#     return render(request,'reportcard.html', {'term1_marks':term1_marks,'term2_marks':term2_marks,'finals_marks':finals_marks})

