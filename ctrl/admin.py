from django.contrib import admin
from .models import repair_cmpt, report,options_std,options_tcher


# Register your models here.
admin.site.register(report)
admin.site.register(repair_cmpt)
admin.site.register(options_std)
admin.site.register(options_tcher)
