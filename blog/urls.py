from django.urls import path
from .views import BlogListView,BlogDetailView

urlpatterns = [
    path('blog_list',BlogListView.as_view(), name = 'blog-list'),
    path('blog_detail/',BlogDetailView.as_view(), name = 'blog-detail'),
]