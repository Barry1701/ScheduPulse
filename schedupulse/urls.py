from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from website.views import welcome, about, register

urlpatterns = [
    path('', welcome, name="welcome"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('meetings/', include('meetings.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('users/', include('users.urls')),

]
