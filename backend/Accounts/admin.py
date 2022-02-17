from django.contrib import admin
from . import models
# View data in model
class ViewAccounts(admin.ModelAdmin):
    list_display = ["Username", "Email"]

# Register your models here.
admin.site.register(models.Account, ViewAccounts)
admin.site.register(models.Employ)