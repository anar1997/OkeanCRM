from calendar import month

from django.forms import ValidationError
from mehsullar.models import Muqavile, Servis, OdemeTarix
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np


@receiver(post_save, sender=Muqavile)
def create_services(sender, instance, created, **kwargs):
    print(f"Created ==> {created}")
    indi = datetime.datetime.today().strftime('%Y-%m-%d')
    month6 = datetime.datetime.today()+ relativedelta(months=6)
    month18 = datetime.datetime.today()+ relativedelta(months=18)
    month24 = datetime.datetime.today()+ relativedelta(months=24)
    print(f'muqavile --> {instance}')
    print(f"indi --> {indi}")
    if created:
        Servis.objects.create(
            muqavile=instance,
            servis_tarix6ay= month6.strftime('%Y-%m-%d'),
            servis_tarix18ay= month18.strftime('%Y-%m-%d'),
            servis_tarix24ay= month24.strftime('%Y-%m-%d'),
        )

@receiver(post_save, sender=Muqavile)
def create_odeme_tarix(sender, instance, created, **kwargs):
    print(f"Created muqavile for odeme tarixleri ==> {created}")
    print(instance.odenis_uslubu)
    print(instance.negd_odenis_1)
    print(instance.negd_odenis_2)
    print(instance.negd_odenis_1_tarix)
    print(instance.negd_odenis_2_tarix)
    kredit_muddeti = instance.kredit_muddeti
    print(f"kredit_muddeti ===> {kredit_muddeti} --- {type(kredit_muddeti)}")

    if(instance.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
        if created:
            i = 0
            while(i<2):
                OdemeTarix.objects.create(
                    muqavile = instance,
                    tarix = f"instance.negd_odenis_{i+1}_tarix",
                    qiymet = float(f"instance.negd_odenis_{i+1}")
                )
                i+=1
    if(instance.odenis_uslubu == "KREDIT"):
        indi = datetime.datetime.today().strftime('%Y-%m-%d')
        print(f"INDI ====> {indi} --- {type(indi)}")
        inc_month = pd.date_range(indi, periods = kredit_muddeti+1, freq='M')
        print(f"inc_month ==> {inc_month} --- {type(inc_month)}")

        ilkin_odenis = instance.ilkin_odenis
        ilkin_odenis_qaliq = instance.ilkin_odenis_qaliq

        print(f"Ilkin odenis ==> {ilkin_odenis}  --- {type(ilkin_odenis)}")
        print(f"Ilkin odenis qaliq ==> {ilkin_odenis_qaliq} --- {type(ilkin_odenis_qaliq)}")

        mehsulun_qiymeti = instance.mehsul.qiymet
        print(f"mehsulun_qiymeti ==> {mehsulun_qiymeti} --- {type(mehsulun_qiymeti)}")

        ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
        print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam} --- {type(ilkin_odenis_tam)}")

        aylara_gore_odenecek_umumi_mebleg = mehsulun_qiymeti - ilkin_odenis_tam
        print(f"aylara_gore_odenecek_umumi_mebleg ==> {aylara_gore_odenecek_umumi_mebleg} --- {type(aylara_gore_odenecek_umumi_mebleg)}")

        aylara_gore_odenecek_mebleg = aylara_gore_odenecek_umumi_mebleg // kredit_muddeti
        print(f"aylara_gore_odenecek_mebleg ==> {aylara_gore_odenecek_mebleg} --- {type(aylara_gore_odenecek_mebleg)}")

        qaliq = aylara_gore_odenecek_mebleg * (kredit_muddeti - 1)
        son_aya_odenecek_mebleg = aylara_gore_odenecek_umumi_mebleg - qaliq
        print(f"son_aya_odenecek_mebleg ==> {son_aya_odenecek_mebleg} --- {type(son_aya_odenecek_mebleg)}")
        print(f"inc_month[0].day ======> {inc_month[0].day}")
        print(f"Datearaerarqa ===> {datetime.date.today().day} --- {type(datetime.date.today().day)}")
        print(f"Son gunu bugune gore ====> {inc_month[1].year}-{inc_month[1].month}-{datetime.date.today().day}",)
        print(f"Son gunu ayin son gunune gore ==>  {inc_month[1].year}-{inc_month[1].month}-{inc_month[1].day}")
        if created:
            i = 1
            while(i<=kredit_muddeti):
                if(i == kredit_muddeti):
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile = instance,
                            tarix = f"{inc_month[i].year}-{inc_month[i].month}-{datetime.date.today().day}",
                            qiymet = son_aya_odenecek_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[i].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile = instance,
                                tarix = f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                                qiymet = son_aya_odenecek_mebleg
                            )
                    
                else:
                    if(datetime.date.today().day < 29):
                        OdemeTarix.objects.create(
                            muqavile = instance,
                            tarix = f"{inc_month[i].year}-{inc_month[i].month}-{datetime.date.today().day}",
                            qiymet = aylara_gore_odenecek_mebleg
                        )
                    elif(datetime.date.today().day == 31 or datetime.date.today().day == 30 or datetime.date.today().day == 29):
                        if(inc_month[i].day <= datetime.date.today().day):
                            OdemeTarix.objects.create(
                                muqavile = instance,
                                tarix = f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                                qiymet = aylara_gore_odenecek_mebleg
                            )
                i+=1