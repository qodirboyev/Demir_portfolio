from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Resume,About_blog


# Create your views here.

class ResumeListView(ListView):
    model = Resume
    template_name = "about_resume_app/resume.html"


class ResumeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Resume
    template_name = "about_resume_app/edit_resume.html"
    fields = ['kasb','about','dev_long','frameworks','database','frontend_t','python_modul',
              'ish_joy','lavozim','vazifalar','ishlash_davri','life_long']

    def test_func(self):
        return self.request.user.is_superuser

class About_blogView(LoginRequiredMixin,ListView):
    model = About_blog
    template_name = "about_resume_app/about.html"


class About_blog_CreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = About_blog
    template_name = "about_resume_app/add_about_blog.html"
    fields = ['image','title','text']

    def test_func(self):
        return self.request.user.is_superuser
