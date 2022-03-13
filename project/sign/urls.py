from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me

urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    # path('login/',
    #      LoginView.as_view(template_name = 'sign/login.html'),
    #      name='login'),#уже не надо так как вход по почте
    #
    # path('signup/',
    #      BaseRegisterView.as_view(template_name = 'sign/signup.html'),
    #      name='signup'),# уже не надо так как регистрация по почте
    path('upgrade/', upgrade_me, name='upgrade'),
]
