from django.contrib import admin
from .models import Appraisement

class AppraisementAdmin(admin.ModelAdmin):
    list_display   = ('created_at', 'code',)
    date_hierarchy = 'created_at'
    ordering       = ('created_at',)
    search_fields  = ('code', 'created_at')

admin.site.register(Appraisement, AppraisementAdmin)
