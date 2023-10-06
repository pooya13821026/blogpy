from django.contrib import admin
from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'auther', 'create_time']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
