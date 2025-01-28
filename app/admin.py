from django.contrib import admin
from .models import UserProfileModel,DoctorProfileModel,MedicalRecordModel
# Register your models here.

admin.site.register(UserProfileModel)
admin.site.register(DoctorProfileModel)
admin.site.register(MedicalRecordModel)
