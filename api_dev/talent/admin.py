from django.contrib import admin
from .models import Talent
# Register your models here.


class TalentAdmin(admin.ModelAdmin):
    list_display = ['name', 'avt', 'dateOfBirth', 'phone', 'regency']


admin.site.register(Talent, TalentAdmin)
