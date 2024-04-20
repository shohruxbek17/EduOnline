from django.shortcuts import render
from django.views import View
from .models import Blog
from course.models import Speciality

class BlogListView(View):
    def get(self,request):
        blog = Blog.objects.all()
        specialitys = Speciality.objects.all()
        context = {
            "blog": blog,
            "specialitys": specialitys
        }
        return render(request, 'main./blog.html', context)


class BlogDetailView(View):
    def get(self,request):
        blog_detail = Blog.objects.all()
        specialitys = Speciality.objects.all()
        context = {
            "blog_detail": blog_detail,
            "specialitys": specialitys
        }
        return render(request, 'main./single.html', context)

