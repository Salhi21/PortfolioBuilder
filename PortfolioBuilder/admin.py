from django.contrib import admin

from PortfolioBuilder.models import User


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields]


admin.site.register(User, EmployeeAdmin)
