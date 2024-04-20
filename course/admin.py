from django.contrib import admin
from .models import Position,Teacher,Course,Speciality,About


admin.site.register(Position)
admin.site.register(Teacher)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','slug_limit','image','description')
    populated_feilds = {'slug_limit': ('title' , )}

    def slug_limit(self,obj):
        return obj.slug[:15]
# admin.site.register(Course)
admin.site.register(Speciality)
admin.site.register(About)