from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import User_edit, Registration
from .models import User
# Register your models here.
class AdminUser(UserAdmin):
    form = User_edit
    add_form = Registration
    model = User
    list_display = ('username', 'first_name', 'age', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(User, AdminUser)



