from mehsullar.models import Muqavile, Servis
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

@receiver(post_save, sender=Muqavile)
def create_services(sender, instance, created, **kwargs):
    print(f"Created ==> {created}")
    indi = f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}"
    month6 = datetime.datetime.now() + datetime.timedelta(days=180)
    month18 = datetime.datetime.now() + datetime.timedelta(days=540)
    month24 = datetime.datetime.now() + datetime.timedelta(days=720)
    print(f'tarix --> {instance}')
    print(f"indi --> {indi}")
    if created:
        Servis.objects.create(
            muqavile=instance,
            servis_tarix6ay=f"{month6.year}-{month6.month}-{datetime.datetime.now().day}",
            servis_tarix18ay=f"{month18.year}-{month18.month}-{datetime.datetime.now().day}",
            servis_tarix24ay=f"{month24.year}-{month24.month}-{datetime.datetime.now().day}",
        )
