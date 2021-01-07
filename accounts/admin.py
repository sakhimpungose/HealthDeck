from django.contrib import admin
from .models import User, Organisation

class OrganisationInline(admin.TabularInline):
    model = Organisation
    fields = ('name', 'description')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'username', 'email', 'date_of_birth', 'gender')
    inlines = (OrganisationInline,)


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass