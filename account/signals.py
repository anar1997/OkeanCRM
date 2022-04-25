from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from maas.models import MaasGoruntuleme
from mehsullar.models import Muqavile
from account.models import IsciSatisSayi, User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import pandas as pd

@receiver(post_save, sender=User)
def create_isci_maas_goruntulenme(sender, instance, created, **kwargs):
    if created:
        user = instance
        print(f"Celery users ==> {user}")
        indi = datetime.date.today()
        print(f"Celery indi ==> {indi}")
        
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")

        next_m = d + pd.offsets.MonthBegin(1)
        print(f"next_m ==> {next_m}")

        
        isci_maas = MaasGoruntuleme.objects.filter(
            isci=user, 
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery isci_maas ==> {isci_maas}")
        if len(isci_maas) == 0:
            if user.maas_uslubu == "FİX":
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{indi.year}-{indi.month}-{1}", yekun_maas=user.maas).save()
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}", yekun_maas=user.maas).save()
            else:    
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{indi.year}-{indi.month}-{1}").save()
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}").save()