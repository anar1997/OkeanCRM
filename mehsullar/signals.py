from django.shortcuts import get_object_or_404
from mehsullar.models import Anbar, Mehsullar, Muqavile, Servis, OdemeTarix, ServisOdeme, Stok
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import pandas as pd
from django.db import transaction

@receiver(post_save, sender=Muqavile)
def create_services(sender, instance, created, **kwargs):
    if created:
        print(f"Created ==> {created}")
        indi = datetime.date.today()
        print(f"Celery indi ==> {indi}")
        
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")

        month6 = d + pd.offsets.MonthBegin(6)
        print(f"month6 ==> {month6}")

        month12 = d + pd.offsets.MonthBegin(12)
        print(f"month12 ==> {month12}")

        month18 = d + pd.offsets.MonthBegin(18)
        print(f"month18 ==> {month18}")

        month24 = d + pd.offsets.MonthBegin(24)
        print(f"month24 ==> {month24}")

        print(f'muqavile --> {instance}')

        print(instance.mehsul_sayi)

        print(f"Muqavile ofis ==> {instance.vanleader.ofis}")
        anbar = get_object_or_404(Anbar, ofis=instance.ofis)
        print(f"Muqavile anbar ==> {anbar}")
        
        kartric6ay = Mehsullar.objects.filter(kartric_novu="KARTRIC6AY")
        kartric12ay = Mehsullar.objects.filter(kartric_novu="KARTRIC12AY")
        kartric18ay = Mehsullar.objects.filter(kartric_novu="KARTRIC18AY")
        kartric24ay = Mehsullar.objects.filter(kartric_novu="KARTRIC24AY")

        print(f'kartric6ay --> {kartric6ay}')
        print(f'kartric12ay --> {kartric12ay}')
        print(f'kartric18ay --> {kartric18ay}')
        print(f'kartric24ay --> {kartric24ay}')

        q = 0
        while(q<instance.mehsul_sayi):
            for i in range(1):
                servis_qiymeti = 0
                for j in kartric6ay:
                    print(f"----------------------------{j=}")
                    servis_qiymeti += float(j.qiymet)
                servis = Servis.objects.create(
                    muqavile=instance,
                    servis_tarix = month6,
                    servis_qiymeti=servis_qiymeti
                )
                servis.mehsullar.set(kartric6ay)
                servis.save()
            for i in range(1):
                servis_qiymeti = 0
                for j in kartric12ay:
                    print(f"----------------------------{j=}")
                    servis_qiymeti += float(j.qiymet)
                servis = Servis.objects.create(
                    muqavile=instance,
                    servis_tarix = month12,
                    servis_qiymeti=servis_qiymeti
                )
                servis.mehsullar.set(kartric12ay)
                servis.save()
            for i in range(1):
                servis_qiymeti = 0
                for j in kartric18ay:
                    print(f"----------------------------{j=}")
                    servis_qiymeti += float(j.qiymet)
                servis = Servis.objects.create(
                    muqavile=instance,
                    servis_tarix = month18,
                    servis_qiymeti=servis_qiymeti
                )
                servis.mehsullar.set(kartric18ay)
                servis.save()
            for i in range(1):
                servis_qiymeti = 0
                for j in kartric24ay:
                    print(f"----------------------------{j=}")
                    servis_qiymeti += float(j.qiymet)
                servis = Servis.objects.create(
                    muqavile=instance,
                    servis_tarix = month24,
                    servis_qiymeti=servis_qiymeti
                )
                servis.mehsullar.set(kartric24ay)
                servis.save()
            q+=1

@receiver(post_save, sender=Servis)
def create_servis_odeme(sender, instance, created, **kwargs):
    if created:
        print(f"----------------------------{instance=}")
        
        servis_odeme = ServisOdeme.objects.create(
            servis = instance,
            servis_qiymeti=instance.servis_qiymeti,
            odenilecek_mebleg=instance.servis_qiymeti
        ).save()
        print(f"----------------------------{servis_odeme=}")

        print(f"{servis_odeme=}")


@receiver(post_save, sender=Muqavile)
def create_odeme_tarix(sender, instance, created, **kwargs):
    if created:
        print(f"Created muqavile for odeme tarixleri ==> {created}")
        kredit_muddeti = instance.kredit_muddeti
        print(f"kredit_muddeti ===> {kredit_muddeti} --- {type(kredit_muddeti)}")

        mehsul_sayi = instance.mehsul_sayi
        print(f"mehsul_sayi ===> {mehsul_sayi} --- {type(mehsul_sayi)}")

        print(f"odenis_uslubu ===> {instance.odenis_uslubu} --- {type(instance.odenis_uslubu)}")
        
        def kredit_muddeti_func(kredit_muddeti, mehsul_sayi):
            kredit_muddeti_yeni = kredit_muddeti * mehsul_sayi
            return kredit_muddeti_yeni

        if(instance.odenis_uslubu == "KREDİT"):
            
            indi = datetime.datetime.today().strftime('%Y-%m-%d')
            print(f"INDI ====> {indi} --- {type(indi)}")
            inc_month = pd.date_range(indi, periods = kredit_muddeti+1, freq='M')
            print(f"inc_month ==> {inc_month} --- {type(inc_month)}")
            
            ilkin_odenis = instance.ilkin_odenis
            ilkin_odenis_qaliq = instance.ilkin_odenis_qaliq

            if(ilkin_odenis is not None):
                print(f"{ilkin_odenis=}")
                ilkin_odenis = float(ilkin_odenis)
            
            if(ilkin_odenis_qaliq is not None):
                print(f"{ilkin_odenis_qaliq=}")
                ilkin_odenis_qaliq = float(ilkin_odenis_qaliq)

            print(f"Ilkin odenis ==> {ilkin_odenis}  --- {type(ilkin_odenis)}")
            print(f"Ilkin odenis qaliq ==> {ilkin_odenis_qaliq} --- {type(ilkin_odenis_qaliq)}")

            mehsulun_qiymeti = instance.muqavile_umumi_mebleg
            print(f"mehsulun_qiymeti ==> {mehsulun_qiymeti} --- {type(mehsulun_qiymeti)}")

            if(ilkin_odenis_qaliq == 0):
                ilkin_odenis_tam = ilkin_odenis
            elif(ilkin_odenis_qaliq != 0):
                ilkin_odenis_tam = ilkin_odenis + ilkin_odenis_qaliq
            print(f"ilkin_odenis_tam ==> {ilkin_odenis_tam} --- {type(ilkin_odenis_tam)}")

            aylara_gore_odenecek_umumi_mebleg = mehsulun_qiymeti - ilkin_odenis_tam
            print(f"aylara_gore_odenecek_umumi_mebleg ==> {aylara_gore_odenecek_umumi_mebleg} --- {type(aylara_gore_odenecek_umumi_mebleg)}")
            
            if(kredit_muddeti > 0):
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