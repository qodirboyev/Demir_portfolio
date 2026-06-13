from django.urls import path
from .views import ProjectListView,ProjectCreateView

urlpatterns = [
    path('',ProjectListView.as_view(), name='projects'),
    path('add_project/',ProjectCreateView.as_view(),name='add_project'),
]