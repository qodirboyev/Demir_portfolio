from  django.urls import path
from .views import ResumeListView, ResumeUpdateView,About_blogView,About_blog_CreateView

urlpatterns = [
    path('resume', ResumeListView.as_view(), name='resume'),
    path('edit_resume/<int:pk>', ResumeUpdateView.as_view(), name='edit_resume'),
    path('about_me/', About_blogView.as_view(), name='about'),
    path('add_blog/', About_blog_CreateView.as_view(), name='add_blog'),
]


