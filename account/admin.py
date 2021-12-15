from django.contrib import admin
from .models import Merkezler, User, Vezifeler
# Register your models here.
admin.site.register(User)
admin.site.register(Vezifeler)
admin.site.register(Merkezler)