from django.urls import path, include
from .views import CourseListView,TeacherListView,AboutViewList,CourseDetailView,CourseUpdateView,CourseDeleteView,AddNewCourse

urlpatterns = [
    path('course/',CourseListView.as_view(), name = 'courses'),
    path('teachers/',TeacherListView.as_view(), name = 'teachers'),
    path('abouts/', AboutViewList.as_view(), name='abouts'),
    path('course/<slug:slug>/',CourseDetailView.as_view(), name='course_detail'),
    path('update/<int:id>/',CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:id>/',CourseDeleteView.as_view(), name='course-delete'),
    path('add_course/',AddNewCourse.as_view(), name='add-course'),
]