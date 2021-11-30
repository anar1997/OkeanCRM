from django.contrib import admin
from .models import User, Vezifeler, UserVezifeler
# Register your models here.
admin.site.register(User)
admin.site.register(Vezifeler)
admin.site.register(UserVezifeler)