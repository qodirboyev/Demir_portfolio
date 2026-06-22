from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.



class ProjectListView(ListView):
    model = Project
    template_name = 'projects_app/projects.html'



class ProjectCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Project
    template_name = 'projects_app/add_project.html'
    fields = ['image','title','text','url']

    def test_func(self):
        return self.request.user.is_superuser
