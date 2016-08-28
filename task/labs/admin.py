from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext as _


# Register your models here.
admin.site.register(Bloodtest)
admin.site.register(Livertest)
admin.site.register(UserProfile)
admin.site.unregister(User)


class MyUserAdmin(UserAdmin):
    staff_fieldsets = (
        # (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        # No permissions
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )

    def change_view(self, request, *args, **kwargs):
        # for non-superuser
        if not request.user.is_superuser:
            try:
                self.fieldsets = self.staff_fieldsets
                response = super(MyUserAdmin, self).change_view(request, *args, **kwargs)
            finally:
                # Reset fieldsets to its original value
                self.fieldsets = UserAdmin.fieldsets
            return response
        else:
            return super(MyUserAdmin, self).change_view(request, *args, **kwargs)


admin.site.register(User, MyUserAdmin)



