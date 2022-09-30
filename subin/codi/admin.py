from django.contrib import admin

from codi.models import Category, Codi

# Register your models here.
class CodiInline(admin.StackedInline):
    model = Codi
    extra = 2
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (CodiInline,)
    list_display = ('id', 'name', 'description')
    
@admin.register(Codi)
class CodiAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt', 'url')