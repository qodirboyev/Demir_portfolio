from django.urls import path
from .views import SignUp_view
urlpatterns = [
    path('signup/', SignUp_view.as_view(), name='signup'),
]