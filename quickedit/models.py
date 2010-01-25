from django.db import models

class TestInlineModel(models.Model):
    edit_this = models.CharField(max_length=12)
    
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(TestInlineModel, AuthorAdmin)
