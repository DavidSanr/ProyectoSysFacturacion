from django.contrib.auth.views import LoginView,LogoutView
from django.urls import include, path

from bases.views import Home

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login/',LoginView.as_view(template_name = 'bases/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name = 'bases/login.html'),name='logout'),
]
