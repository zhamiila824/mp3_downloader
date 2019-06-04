from django.contrib import admin
from .models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ("url", "email", 'date')
    readonly_fields = ("url", "email", 'date')


admin.site.register(Request, RequestAdmin)
