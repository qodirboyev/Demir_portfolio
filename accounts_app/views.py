from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import Registration
from django.urls import reverse_lazy
# Create your views here.

class SignUp_view(CreateView):
    model = User
    form_class = Registration
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')