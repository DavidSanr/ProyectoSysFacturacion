from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

# Create your views here.

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'base/base.html'
    login_url = 'bases:login'
