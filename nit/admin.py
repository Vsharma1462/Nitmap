from django.contrib import admin
from nit.models import Client,Project

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display=['client_name','created_at','updated_at','created_by']

class ProjectAdmin(admin.ModelAdmin):
    list_display=['project_name','client','created_at','created_by']


admin.site.register(Client,ClientAdmin)
admin.site.register(Project,ProjectAdmin)  
            

