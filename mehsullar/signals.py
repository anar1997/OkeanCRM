from mehsullar.models import Muqavile, Servis, OdemeTarix
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

@receiver(post_save, sender=Muqavile)
def create_services(sender, instance, created, **kwargs):
    print(f"Created ==> {created}")
    indi = datetime.datetime.today().strftime('%Y-%m-%d')
    month6 = datetime.datetime.today()+ relativedelta(months=6)
    month18 = datetime.datetime.today()+ relativedelta(months=18)
    month24 = datetime.datetime.today()+ relativedelta(months=24)
    print(f'muqavile --> {instance}')
    print(f"indi --> {indi}")
    print(instance.mehsul_sayi)
    i = 0
    while(i<instance.mehsul_sayi):
        if created:
            Servis.objects.create(
                muqavile=instance,
                servis_tarix6ay= month6.strftime('%Y-%m-%d'),
                servis_tarix18ay= month18.strftime('%Y-%m-%d'),
                servis_tarix24ay= month24.strftime('%Y-%m-%d'),
            )
        i+=1

@receiver(post_save, sender=Muqavile)
def create_odeme_tarix(sender, instance, created, **kwargs):
    print(f"Created muqavile for odeme tarixleri ==> {created}")
    kredit_muddeti = instance.kredit_muddeti
    print(f"kredit_muddeti ===> {kredit_muddeti} --- {type(kredit_muddeti)}")

    mehsul_sayi = instance.mehsul_sayi
    print(f"mehsul_sayi ===> {mehsul_sayi} --- {type(mehsul_sayi)}")

    print(f"odenis_uslubu ===> {instance.odenis_uslubu} --- {type(instance.odenis_uslubu)}")
    
    def kredit_muddeti_func(kredit_muddeti, mehsul_sayi):
        kredit_muddeti_yeni = kredit_muddeti * mehsul_sayi
        return kredit_muddeti_yeni


    # if(instance.odenis_uslubu == "İKİ DƏFƏYƏ NƏĞD"):
    #     if created:
    #         i = 0
    #         while(i<2):
    #             if(i==0):
    #                 OdemeTarix.objects.create(
    #                     muqavile = instance,
    #                     tarix = instance.negd_odenis_1_tarix,
    #                     qiymet = instance.negd_odenis_1
    #                 )
    #             if(i==1):
    #                 OdemeTarix.objects.create(
    #                     muqavile = instance,
    #                     tarix = instance.negd_odenis_2_tarix,
    #                     qiymet = instance.negd_odenis_2
    #                 )
    #             i+=1
    if(instance.odenis_uslubu == "KREDİT"):
        if created:
            indi = datetime.datetime.today().strftime('%Y-%m-%d')
            print(f"INDI ====> {indi} --- {type(indi)}")
            inc_month = pd.date_range(indi, periods = kredit_muddeti+1, freq='M')
            print(f"inc_month ==> {inc_month} --- {type(inc_month)}")
            
            ilkin_odenis = instance.ilkin_odenis
            ilkin_odenis_qaliq = instance.ilkin_odenis_qaliq

            if(ilkin_odenis != ""):
                ilkin_odenis = float(ilkin_odenis)
            
            if(ilkin_odenis_qaliq != ""):
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