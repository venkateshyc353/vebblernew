from django.contrib import admin
from . models import vebbler_coustmer_info as vc,vebbler_ios_services as ios,vebbler_jobinfo as v_j
from . models import vebblerservice as vs

class v_coustmerinfo(admin.ModelAdmin):
    list_display = ['name','addres','contact','email']

class v_job(admin.ModelAdmin):
    list_display=['name','feedback','mobile','addres']

class v_ios(admin.ModelAdmin):
    list_display = ['company','name','device']

class v_service(admin.ModelAdmin):
    list_display = ['name','date','cost','contact']


admin.site.register(vc,v_coustmerinfo)
admin.site.register(ios,v_ios)
admin.site.register(v_j,v_job)
admin.site.register(vs,v_service)