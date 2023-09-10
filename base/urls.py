from django.urls import path
from .views import CustomLoginView, HomeView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]