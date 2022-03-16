from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from mehsullar.models import Muqavile
from account.models import IsciSatisSayi
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


@receiver(post_save, sender=Muqavile)
def create_isci_satis_sayi(sender, instance, created, **kwargs):
    if created:
        print(f"Created isci satis sayi ==> {created}")
        vanleader = instance.vanleader
        dealer = instance.dealer
        print(f"vanleader ==> {vanleader}")
        print(f"dealer ==> {dealer}")

        mehsul_sayi = instance.mehsul_sayi
        print(f"mehsul_sayi ==> {mehsul_sayi}")

        muqavile_tarixi = instance.muqavile_tarixi
        print(f"muqavile_tarixi ==> {muqavile_tarixi} -- {type(muqavile_tarixi)}")
        
        year = muqavile_tarixi.year
        month = muqavile_tarixi.month
        print(f"year ==> {year} -- {type(year)}")
        print(f"month ==> {month} -- {type(month)}")

        tarix = datetime.date(year=year, month=month, day=1)
        print(f"tarix ==> {tarix} -- {type(tarix)}")

        vanleader_satis_sayi_model = IsciSatisSayi.objects.filter(tarix=tarix, isci = vanleader)
        dealer_satis_sayi_model = IsciSatisSayi.objects.filter(tarix=tarix, isci = dealer)

        print(f"vanleader_satis_sayi_model ==> {vanleader_satis_sayi_model} -- {len(vanleader_satis_sayi_model)}")
        print(f"dealer_satis_sayi_model ==> {dealer_satis_sayi_model} -- {len(dealer_satis_sayi_model)}")
        
        
        if(len(vanleader_satis_sayi_model) == 0):
            vanleader_satis_sayi = IsciSatisSayi.objects.create(tarix=tarix, isci = vanleader, satis_sayi = mehsul_sayi)
            vanleader_satis_sayi.save()
            print(f"vanleader_satis_sayi -- {vanleader_satis_sayi}")
        elif(len(vanleader_satis_sayi_model) != 0):
            vanleader_satis_sayi = vanleader_satis_sayi_model[0]
            print(f"vanleader_satis_sayi -- {vanleader_satis_sayi}")
            vanleader_satis_sayi.satis_sayi = float(vanleader_satis_sayi.satis_sayi) + float(mehsul_sayi)
            vanleader_satis_sayi.save()


        if(len(dealer_satis_sayi_model) == 0):
            dealer_satis_sayi = IsciSatisSayi.objects.create(tarix=tarix, isci = dealer, satis_sayi = mehsul_sayi)
            dealer_satis_sayi.save()
            print(f"dealer_satis_sayi -- {dealer_satis_sayi}")
        elif(len(dealer_satis_sayi_model) != 0):
            dealer_satis_sayi = dealer_satis_sayi_model[0]
            print(f"dealer_satis_sayi -- {dealer_satis_sayi}")
            dealer_satis_sayi.satis_sayi = float(dealer_satis_sayi.satis_sayi) + float(mehsul_sayi)
            dealer_satis_sayi.save()