from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Blood)
admin.site.register(models.FindByClothe)
admin.site.register(models.FindById)
admin.site.register(models.Hospital)
admin.site.register(models.HospitalUser)
admin.site.register(models.Room)
