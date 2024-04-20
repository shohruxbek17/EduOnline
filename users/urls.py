from django.urls import path
from .views import LandindPageView,RegisterListView

urlpatterns = [
    path("", LandindPageView.as_view(), name = 'landing'),
    path("login", RegisterListView.as_view(), name = 'register'),

]