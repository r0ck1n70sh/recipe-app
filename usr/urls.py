from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='usr-register'),
    path('login/', auth_views.LoginView.as_view(template_name='usr/login.html'), name='usr-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usr/logout.html'), name='usr-logout'),
    path('profile/', views.profile, name='usr-profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)