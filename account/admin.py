from django.contrib import admin
from .models import Ofis, User, Vezifeler, Shirket, Shobe, Musteri, MusteriQeydler
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(User)
admin.site.register(Vezifeler)
admin.site.register(Ofis)
admin.site.register(Shirket)
admin.site.register(Shobe)
admin.site.register(Musteri)
admin.site.register(MusteriQeydler)

admin.site.register(Permission)