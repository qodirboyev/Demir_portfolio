from django.urls import path
from .views import Family,Family_blogCreate,Logo_list,Logo_Create

urlpatterns = [
    path('family/',Family.as_view(),name='family'),
    path('add_family_blog/',Family_blogCreate.as_view(),name='add_family_blog'),
    path('logo/',Logo_list.as_view(),name='logo'),
    path('add_logo/',Logo_Create.as_view(),name='add_logo'),
]