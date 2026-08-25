from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'stock', 'status', 'location', 'updated_at')
    list_filter = ('category', 'status')
    search_fields = ('code', 'name')