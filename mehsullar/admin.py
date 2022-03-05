from django.contrib import admin
from .models import Anbar,Mehsullar, AnbarQeydler, Emeliyyat, Muqavile, OdemeTarix, Servis, Stok


class OdemeTarixAdmin(admin.ModelAdmin):
    list_filter = [
        "muqavile",
        'muqavile__odenis_uslubu',
        'odenme_status',
        'sifira_gore_odeme_status',
        'natamama_gore_odeme_status',
    ]
    search_fields = (
        "muqavile",
    )

# Register your models here.
admin.site.register(Mehsullar)
admin.site.register(Anbar)
admin.site.register(AnbarQeydler)
admin.site.register(Emeliyyat)
admin.site.register(Muqavile)
admin.site.register(OdemeTarix, OdemeTarixAdmin)
admin.site.register(Servis)
admin.site.register(Stok)