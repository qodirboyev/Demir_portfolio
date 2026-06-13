from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Family_blog,Logo


# Create your views here.


class Family(LoginRequiredMixin,ListView):
    model = Family_blog
    template_name = 'family_logo_app/family.html'


class Family_blogCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Family_blog
    template_name = 'family_logo_app/add_family_blog.html'
    fields = ['image','title','text']

    def test_func(self):
        return self.request.user.is_superuser


class Logo_list(LoginRequiredMixin,ListView):
    model = Logo
    template_name = 'family_logo_app/logo.html'

class Logo_Create(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Logo
    template_name = 'family_logo_app/add_logo.html'
    fields = ['image','title','text']
    def test_func(self):
        return self.request.user.is_superuser