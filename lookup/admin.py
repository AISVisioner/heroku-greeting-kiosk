from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    readonly_fields = ('recent_access_at','created_at',)