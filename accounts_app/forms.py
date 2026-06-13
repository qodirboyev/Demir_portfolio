from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'last_name', 'first_name']

class User_edit(UserChangeForm):
    class Meta:
        model = User
        fields = ['age', 'last_name', 'first_name']


