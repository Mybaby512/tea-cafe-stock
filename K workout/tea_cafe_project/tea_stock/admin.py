from django.contrib import admin
from .models import Category, TeaItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(TeaItem)
class TeaItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'updated_at')
    list_filter = ('category', 'updated_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')  # แก้ไขราคาและสต็อกด่วนๆ ได้จากหน้าตารางแอดมินเลย
    ordering = ('-updated_at',)