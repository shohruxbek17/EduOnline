from django.shortcuts import render
from django.views import View
from course.models import Course,Speciality,Teacher
from blog.models import Blog
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LandindPageView(View):
    def get(self,request):
        specialitys = Speciality.objects.all()
        courses = Course.objects.filter(status = 'pb')
        teacher = Teacher.objects.all()
        blogs = Blog.objects.all()
        context = {
            "specialitys": specialitys,
            "courses": courses,
            "teacher": teacher,
            "blogs": blogs,
            "active": {
                "home":"active",
                "about":None,
                "course":None,
                "teacher":None,
            }
        }

        return render(request,'main./index.html',context)

class AboutListView(View):
    def get(self,request):
        courses = Course.objects.all()
        context = {
            "courses": courses,
        }
        return render(request, 'main./index.html', context)


# Inside views.py
class RegisterListView(View):
    def get(self,request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')  # Redirect to your home page
        else:
            form = RegistrationForm()
        return render(request, 'main/registration.html', {'form': form})
