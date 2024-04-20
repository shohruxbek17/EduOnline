from django.shortcuts import render,redirect
from django.views import View
from .models import Course,Teacher,About,Speciality

class CourseListView(View):
    def get(self,request):
        search = request.GET.get("search")
        specialitys = Speciality.objects.all()
        if not search:
            courses = Course.objects.filter(status = 'pb')
            context = {
                "courses": courses,
                "res": search,
                "specialitys" :specialitys,
                "active": {
                        "home":None,
                        "about":None,
                        "course":"active",
                        "teacher":None,
                    }
            }
            return render(request, 'main./course.html', context)
        else:
            courses = Course.objects.filter(title__icontains=search,status = 'pb')
            if courses:
                context = {
                    "courses": courses,
                    "res": search,
                    "specialitys": specialitys,
                    "active": {
                        "home":None,
                        "about":None,
                        "course":"active",
                        "teacher":None,
                    }
                }
                return render(request, 'main./course.html', context)
            else:
                context = {
                    "courses": courses,
                    "res": search,
                    "specialitys": specialitys,
                    "active": {
                        "home":None,
                        "about":None,
                        "course":"active",
                        "teacher":None,
                    }
                }
                return render(request, 'main./course.html', context)


class AboutViewList(View):
    def get(self,request):
        abouts = About.objects.all()
        specialitys = Speciality.objects.all()
        context = {
            "abouts": abouts,
            "specialitys": specialitys,
            "active": {
                "home": None,
                "about": "active",
                "course":None,
                "teacher": None,
            }
        }
        return render(request, 'main./about.html', context)

class TeacherListView(View):
    def get(self,request):
        teacher = Teacher.objects.all()
        specialitys = Speciality.objects.all()
        context = {
            "teacher": teacher,
            "specialitys": specialitys,
            "active": {
                "home": None,
                "about":None,
                "course": None,
                "teacher":"active"
            }
        }
        return render(request, 'main./teacher.html', context)

class CourseDetailView(View):
    def get(self,request,slug):
        course = Course.objects.get(slug=slug)
        return render(request,"course_detail.html" ,{"course":course})

class CourseUpdateView(View):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        return render(request,'course_update.html',{"course":course})


    def post(self,request,id):
        new_title = request.POST.get("title")
        new_description = request.POST.get("description")
        new_price = request.POST.get("price")
        # id = request.POST.get("id")

        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()

        return redirect("courses")

class CourseDeleteView(View):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        course.delete()

        return redirect("courses")

class AddNewCourse(View):
    def get(self,request):
        return render(request,'add_new_course.html')

    def post(self,request):
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.POST.get("image")

        course = Course(title=title,description=description,price=price,image=f"course/course/{image}")
        course.save()
        return redirect('courses')