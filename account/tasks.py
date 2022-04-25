import datetime

from company.models import Vezifeler
from .models import User
from maas.models import CanvasserPrim, MaasGoruntuleme, OfficeLeaderPrim, VanLeaderPrim
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

@shared_task(name='isci_fix_maas_auto_elave_et')
def isci_fix_maas_auto_elave_et():
    indi = datetime.date.today()
    print(f"Celery indi ==> {indi}")

    bu_ay = f"{indi.year}-{indi.month}-{1}"
    
    d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
    print(f"d ==> {d}")

    evvelki_ay = d - pd.offsets.MonthBegin(1)
    print(f"evvelki_ay ==> {evvelki_ay}")

    officeLeaderVezife = Vezifeler.objects.get(vezife_adi="OFFICE LEADER")
    print(f"{officeLeaderVezife=}")
    officeLeaders = User.objects.filter(vezife=officeLeaderVezife)
    print(f"{officeLeaders=}")

    for officeLeader in officeLeaders:
        officeLeader_status = officeLeader.isci_status
        print(f"{officeLeader_status=}")

        ofisleader_prim = OfficeLeaderPrim.objects.get(prim_status=officeLeader_status)
        print(f"{ofisleader_prim=}")

        officeLeader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=bu_ay)
        print(f"{officeLeader_maas_goruntulenme_bu_ay=}")


        officeLeader_maas_goruntulenme_bu_ay.yekun_maas = float(officeLeader_maas_goruntulenme_bu_ay.yekun_maas) + float(ofisleader_prim.fix_maas)
        print(f"{officeLeader_maas_goruntulenme_bu_ay.yekun_maas=}")
        officeLeader_maas_goruntulenme_bu_ay.save()
    
    vanLeaderVezife = Vezifeler.objects.get(vezife_adi="VAN LEADER")
    print(f"{vanLeaderVezife=}")
    vanLeaders = User.objects.filter(vezife=vanLeaderVezife)
    print(f"{vanLeaders=}")

    for vanleader in vanLeaders:
        vanleader_status = vanleader.isci_status
        print(f"{vanleader_status=}")

        vanleader_prim = VanLeaderPrim.objects.get(prim_status=vanleader_status, odenis_uslubu="NƏĞD")
        print(f"{vanleader_prim=}")

        vanleader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=vanleader, tarix=bu_ay)
        print(f"{vanleader_maas_goruntulenme_bu_ay=}")

        vanleader_maas_goruntulenme_bu_ay.yekun_maas = float(vanleader_maas_goruntulenme_bu_ay.yekun_maas) + float(vanleader_prim.fix_maas)
        print(f"{vanleader_maas_goruntulenme_bu_ay.yekun_maas=}")
        vanleader_maas_goruntulenme_bu_ay.save()

    canvasserVezife = Vezifeler.objects.get(vezife_adi="CANVASSER")
    print(f"{canvasserVezife=}")
    canvassers = User.objects.filter(vezife=canvasserVezife)
    print(f"{canvassers=}")

    for canvesser in canvassers:
        canvesser_status = canvesser.isci_status
        print(f"{canvesser_status=}")

        canvesser_prim = CanvasserPrim.objects.get(prim_status=canvesser_status)
        print(f"{canvesser_prim=}")

        canvesser_maas_goruntulenme_evvelki_ay = MaasGoruntuleme.objects.get(isci=canvesser, tarix=evvelki_ay)
        canvesser_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=canvesser, tarix=f"{indi.year}-{indi.month}-{1}")
        print(f"{canvesser_maas_goruntulenme_evvelki_ay=}")
        print(f"{canvesser_maas_goruntulenme_bu_ay=}")

        satis_sayina_gore_prim = 0
        if (canvesser_maas_goruntulenme_evvelki_ay.satis_sayi == 0):
            satis_sayina_gore_prim = canvesser_prim.satis0
        elif (canvesser_maas_goruntulenme_evvelki_ay.satis_sayi >= 1) and (canvesser_maas_goruntulenme_evvelki_ay.satis_sayi <= 8):
            satis_sayina_gore_prim = canvesser_prim.satis1_8

        canvesser_maas_goruntulenme_bu_ay.yekun_maas = float(canvesser_maas_goruntulenme_bu_ay.yekun_maas) + float(satis_sayina_gore_prim) + float(canvesser_prim.fix_maas)
        print(f"{canvesser_maas_goruntulenme_bu_ay.yekun_maas=}")
        canvesser_maas_goruntulenme_bu_ay.save()
        canvesser_maas_goruntulenme_evvelki_ay.save()