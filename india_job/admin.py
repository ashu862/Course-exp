from django.contrib import admin
from . models import Jobs, Resume, Inquiry, Mail
# Register your models here.
admin.site.register(Jobs)
admin.site.register(Resume)
admin.site.register(Inquiry)
admin.site.register(Mail)