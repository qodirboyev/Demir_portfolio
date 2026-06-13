from django.urls import path
from .views import HomeCommentStatsView,Comments_view,CreateComment_view,UpdateComment_view,DeleteComment_view
urlpatterns = [
    path('', HomeCommentStatsView.as_view(), name='home'),
    path('comments/', Comments_view.as_view(), name='comments'),
    path('add_comment/', CreateComment_view.as_view(), name='add_comment'),
    path('edit_comment/<int:pk>/', UpdateComment_view.as_view(), name='edit_comment'),
    path('delete_comment/<int:pk>/', DeleteComment_view.as_view(), name='delete_comment'),
]
