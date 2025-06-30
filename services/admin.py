from django.contrib import admin
from .models import  (
    Complaint
)
# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['title','id']



admin.site.register(Complaint, ComplaintAdmin)


