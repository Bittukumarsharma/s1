from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=['id','username','email','password','created_at','updated_at'] 
admin.site.register(Person,PersonAdmin)   

