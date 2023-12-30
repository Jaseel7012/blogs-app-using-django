from django.contrib import admin
from . import models

class PostModelAdmin(admin.ModelAdmin):
    list_display=('title','date_created','author')

# Register your models here.
admin.site.register(models.PostModel,PostModelAdmin)
admin.site.register(models.CommentModel)