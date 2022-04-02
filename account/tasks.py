import datetime
from .models import User
from maas.models import MaasGoruntuleme
from celery import shared_task

@shared_task(name='maas_goruntuleme_create_task')
def maas_goruntuleme_create_task():
    users = User.objects.all()
    print(f"Celery users ==> {users}")
    indi = datetime.date.today()
    print(f"Celery indi ==> {indi}")
    for user in users:
        isci_maas = MaasGoruntuleme.objects.filter(
            isci=user, 
            tarix__year = indi.year,
            tarix__month = indi.month
        )
        print(f"Celery isci_maas ==> {isci_maas}")
        if len(isci_maas) != 0:
            continue
        else:
            MaasGoruntuleme.objects.create(isci=user).save()

@shared_task(name='maas_goruntuleme_create_task_15')
def maas_goruntuleme_create_task_15():
    users = User.objects.all()
    print(f"Celery users ==> {users}")
    indi = datetime.date.today()
    print(f"Celery indi ==> {indi}")
    for user in users:
        isci_maas = MaasGoruntuleme.objects.filter(
            isci=user, 
            tarix__year = indi.year,
            tarix__month = indi.month
        )
        print(f"Celery isci_maas ==> {isci_maas}")
        if len(isci_maas) != 0:
            print("Iscinin bu ay ucun maas karti var")
            continue
        else:
            print("Isci maas karti create oldu")
            MaasGoruntuleme.objects.create(isci=user).save()