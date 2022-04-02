import datetime
from .models import User
from maas.models import MaasGoruntuleme
from celery import shared_task
import pandas as pd

@shared_task(name='maas_goruntuleme_create_task')
def maas_goruntuleme_create_task():
    users = User.objects.all()
    print(f"Celery users ==> {users}")
    indi = datetime.date.today()
    print(f"Celery indi ==> {indi}")
    
    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    for user in users:
        isci_maas = MaasGoruntuleme.objects.filter(
            isci=user, 
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery isci_maas ==> {isci_maas}")
        if len(isci_maas) != 0:
            continue
        else:
            if user.maas_uslubu == "FİX": 
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}", yekun_maas=user.maas).save()
            else:    
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}").save()

@shared_task(name='maas_goruntuleme_create_task_15')
def maas_goruntuleme_create_task_15():
    users = User.objects.all()
    print(f"Celery users ==> {users}")
    indi = datetime.date.today()
    print(f"Celery indi ==> {indi}")
    
    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    next_m = d + pd.offsets.MonthBegin(1)
    print(f"next_m ==> {next_m}")

    for user in users:
        isci_maas = MaasGoruntuleme.objects.filter(
            isci=user, 
            tarix__year = next_m.year,
            tarix__month = next_m.month
        )
        print(f"Celery isci_maas ==> {isci_maas}")
        if len(isci_maas) != 0:
            continue
        else:
            if user.maas_uslubu == "FİX": 
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}", yekun_maas=user.maas).save()
            else:    
                MaasGoruntuleme.objects.create(isci=user, tarix=f"{next_m.year}-{next_m.month}-{1}").save()
