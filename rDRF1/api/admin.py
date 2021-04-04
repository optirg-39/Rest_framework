from django.contrib import admin
from .models import Students


@admin.register(Students)
class Studentsadmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

# admin.site.register(Students)
# Register your models here.



