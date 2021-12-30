from django.contrib import admin
from .models import Merkezler, User, Vezifeler, Shirket, Shobe, Musteri, MusteriQeydler
# Register your models here.
admin.site.register(User)
admin.site.register(Vezifeler)
admin.site.register(Merkezler)
admin.site.register(Shirket)
admin.site.register(Shobe)
admin.site.register(Musteri)
admin.site.register(MusteriQeydler)

