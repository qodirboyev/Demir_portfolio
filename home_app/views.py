from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Avg, Count

class HomeCommentStatsView(TemplateView):
    template_name = "./home_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_comments"] = Comment.objects.count()
        context["total_users"] = Comment.objects.values("user").distinct().count()
        context["average_rating"] = round(Comment.objects.aggregate(Avg("rating"))["rating__avg"] or 0, 1)
        return context

class Comments_view(LoginRequiredMixin,ListView):
    model = Comment
    template_name = 'home_app/comments.html'


class CreateComment_view(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "home_app/add_comment.html"
    fields = ['text','rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateComment_view(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    template_name = "home_app/comment_edit.html"
    fields = ['text','rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class DeleteComment_view(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = "home_app/delete_comment.html"
    success_url = reverse_lazy('comments')
    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user

