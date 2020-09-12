from django.contrib import admin
from .models import repair_cmpt, report


# Register your models here.
admin.site.register(report)
admin.site.register(repair_cmpt)