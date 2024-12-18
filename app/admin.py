from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.FacultyDetails)
admin.site.register(models.HODDetails)
admin.site.register(models.AdminDetails)

# admin.site.register(models.Finals)
# admin.site.register(models.Term1)
# admin.site.register(models.Term2)
