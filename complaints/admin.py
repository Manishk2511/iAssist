from django.contrib import admin
from .models import complaint, problem, otp_verification, image_upload, Complaints
# Register your models here.
admin.site.register(complaint),
admin.site.register(Complaints),
admin.site.register(problem),
admin.site.register(otp_verification)
admin.site.register(image_upload)
