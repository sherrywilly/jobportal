from django.contrib import admin
from .models import JobRequest, StudentExtra, RecruterExtra, Job


class StudentExtraAdmin(admin.ModelAdmin):
    pass


admin.site.register(StudentExtra, StudentExtraAdmin)


class RecruterExtraAdmin(admin.ModelAdmin):
    pass


admin.site.register(RecruterExtra, RecruterExtraAdmin)
admin.site.register(Job)
admin.site.register(JobRequest)
