from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
	list_display = ['created_at', 'user', 'title','updated_at']

admin.site.register(Post,PostAdmin)