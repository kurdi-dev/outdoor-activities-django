from django.contrib import admin

# Register your models here.
from .models import Activity, Category, Message
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(Message)