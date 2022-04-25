from django.db.models.signals import post_save
from django.dispatch import receiver

import pandas as pd
import datetime

from account.models import User
from company.models import Vezifeler
from maas.models import CanvasserPrim, DealerPrim, MaasGoruntuleme, OfficeLeaderPrim, VanLeaderPrim
from mehsullar.models import Muqavile

@receiver(post_save, sender=Muqavile)
def create_prim(sender, instance, created, **kwargs):
    if created:
        indi = datetime.date.today()
        print(f"indi ==> {indi}")
        d = pd.to_datetime(f"{indi.year}-{indi.month}-{1}")
        print(f"d ==> {d}")
        next_m = d + pd.offsets.MonthBegin(1)
        print(f"next_m ==> {next_m}")
        days_in_mont = pd.Period(f"{next_m.year}-{next_m.month}-{1}").days_in_month
        print(f"days_in_mont ==> {days_in_mont}")
        
        muqavile_odenis_uslubu = instance.odenis_uslubu
        print(f"{muqavile_odenis_uslubu=}")

        vanleader = instance.vanleader
        print(f"{vanleader=}")
        if vanleader is not None:
            vanleader_status = vanleader.isci_status
            print(f"{vanleader_status=}")
        else:
            vanleader_status = None

        dealer = instance.dealer
        print(f"{dealer=}")
        if dealer is not None:
            dealer_status = dealer.isci_status
            print(f"{dealer_status=}")
            dealer_vezife_l = dealer.vezife.all()
            for v in dealer_vezife_l:
                dealer_vezife = v.vezife_adi
            print(f"{dealer_vezife=} -- {type(dealer_vezife)}")
        else:
            dealer_status = None
            dealer_vezife = None


        canvesser = instance.canvesser
        print(f"{canvesser=}")
        if canvesser is not None:
            canvesser_status = canvesser.isci_status
            print(f"{canvesser_status=}")
            canvesser_vezife_l = canvesser.vezife.all()
            for i in canvesser_vezife_l:
                canvesser_vezife = i.vezife_adi
            print(f"{canvesser_vezife=} -- {type(canvesser_vezife)}")
        else:
            canvesser_status = None
            canvesser_vezife = None

        ofis = instance.ofis
        print(f"{ofis=}")
        if (ofis is not None) or (ofis != ""):
            officeLeaderVezife = Vezifeler.objects.get(vezife_adi="OFFICE LEADER")
            print(f"{officeLeaderVezife=}")
            officeLeaders = User.objects.filter(ofis=ofis, vezife=officeLeaderVezife)
            print(f"{officeLeaders=}")

            for officeLeader in officeLeaders:
                officeLeader_status = officeLeader.isci_status
                print(f"{officeLeader_status=}")
                ofisleader_prim = OfficeLeaderPrim.objects.get(prim_status=officeLeader_status)
                print(f"{ofisleader_prim=}")

                officeLeader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=f"{indi.year}-{indi.month}-{1}")
                officeLeader_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=officeLeader, tarix=next_m)
                print(f"{officeLeader_maas_goruntulenme_bu_ay=}")
                print(f"{officeLeader_maas_goruntulenme_novbeti_ay=}")

                officeLeader_maas_goruntulenme_bu_ay.satis_sayi = float(officeLeader_maas_goruntulenme_bu_ay.satis_sayi) + float(instance.mehsul_sayi)
                officeLeader_maas_goruntulenme_bu_ay.satis_meblegi = float(officeLeader_maas_goruntulenme_bu_ay.satis_meblegi) + (float(instance.mehsul.qiymet) * float(instance.mehsul_sayi))
                print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_sayi=}")
                print(f"{officeLeader_maas_goruntulenme_bu_ay.satis_meblegi=}")
                officeLeader_maas_goruntulenme_bu_ay.save()

                officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas = float(officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas) + (float(ofisleader_prim.ofise_gore_prim) * float(instance.mehsul_sayi))
                print(f"{officeLeader_maas_goruntulenme_novbeti_ay.yekun_maas=}")
                officeLeader_maas_goruntulenme_novbeti_ay.save()

        # --------------------------------------------------------
        if (vanleader_status is not None):
            vanleader_prim = VanLeaderPrim.objects.get(prim_status=vanleader_status, odenis_uslubu=muqavile_odenis_uslubu)
            print(f"{vanleader_prim=}")

            vanleader_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=vanleader, tarix=f"{indi.year}-{indi.month}-{1}")
            vanleader_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=vanleader, tarix=next_m)
            print(f"{vanleader_maas_goruntulenme_bu_ay=}")
            print(f"{vanleader_maas_goruntulenme_novbeti_ay=}")

            vanleader_maas_goruntulenme_bu_ay.satis_sayi = float(vanleader_maas_goruntulenme_bu_ay.satis_sayi) + float(instance.mehsul_sayi)
            vanleader_maas_goruntulenme_bu_ay.satis_meblegi = float(vanleader_maas_goruntulenme_bu_ay.satis_meblegi) +  (float(instance.mehsul.qiymet) * float(instance.mehsul_sayi))
            print(f"{vanleader_maas_goruntulenme_bu_ay.satis_sayi=}")
            print(f"{vanleader_maas_goruntulenme_bu_ay.satis_meblegi=}")

            vanleader_maas_goruntulenme_bu_ay.save()

            vanleader_maas_goruntulenme_novbeti_ay.yekun_maas = float(vanleader_maas_goruntulenme_novbeti_ay.yekun_maas) + (float(vanleader_prim.komandaya_gore_prim) * float(instance.mehsul_sayi))
            print(f"{vanleader_maas_goruntulenme_novbeti_ay.yekun_maas=}")

            vanleader_maas_goruntulenme_novbeti_ay.save()
            
        # --------------------------------------------------------

        if (dealer_vezife == "DEALER"):
            dealer_prim = DealerPrim.objects.get(prim_status=dealer_status, odenis_uslubu=muqavile_odenis_uslubu)
            print(f"{dealer_prim=}")

            dealer_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=dealer, tarix=f"{indi.year}-{indi.month}-{1}")
            dealer_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=dealer, tarix=next_m)
            print(f"{dealer_maas_goruntulenme_bu_ay=}")
            print(f"{dealer_maas_goruntulenme_novbeti_ay=}")

            dealer_maas_goruntulenme_bu_ay.satis_sayi = float(dealer_maas_goruntulenme_bu_ay.satis_sayi) + float(instance.mehsul_sayi)
            dealer_maas_goruntulenme_bu_ay.satis_meblegi = float(dealer_maas_goruntulenme_bu_ay.satis_meblegi) +  (float(instance.mehsul.qiymet) * float(instance.mehsul_sayi))
            print(f"{dealer_maas_goruntulenme_bu_ay.satis_sayi=}")
            print(f"{dealer_maas_goruntulenme_bu_ay.satis_meblegi=}")

            dealer_maas_goruntulenme_bu_ay.save()


            dealer_maas_goruntulenme_novbeti_ay.yekun_maas = float(dealer_maas_goruntulenme_novbeti_ay.yekun_maas) + (float(dealer_prim.komandaya_gore_prim) * float(instance.mehsul_sayi))
            print(f"{dealer_maas_goruntulenme_novbeti_ay.yekun_maas=}")

            dealer_maas_goruntulenme_novbeti_ay.save()

        # --------------------------------------------------------
        
        if (canvesser_vezife == "CANVASSER"):
            canvesser_prim = CanvasserPrim.objects.get(prim_status=canvesser_status)
            print(f"{canvesser_prim=}")

            canvesser_maas_goruntulenme_bu_ay = MaasGoruntuleme.objects.get(isci=canvesser, tarix=f"{indi.year}-{indi.month}-{1}")
            canvesser_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=canvesser, tarix=next_m)
            print(f"{canvesser_maas_goruntulenme_bu_ay=}")
            print(f"{canvesser_maas_goruntulenme_novbeti_ay=}")

            canvesser_maas_goruntulenme_bu_ay.satis_sayi = float(canvesser_maas_goruntulenme_bu_ay.satis_sayi) + float(instance.mehsul_sayi)
            canvesser_maas_goruntulenme_bu_ay.satis_meblegi = float(canvesser_maas_goruntulenme_bu_ay.satis_meblegi) +  (float(instance.mehsul.qiymet) * float(instance.mehsul_sayi))
            print(f"{canvesser_maas_goruntulenme_bu_ay.satis_sayi=}")
            print(f"{canvesser_maas_goruntulenme_bu_ay.satis_meblegi=}")
            canvesser_maas_goruntulenme_bu_ay.save()

            satis_sayina_gore_prim = 0
            
            if (canvesser_maas_goruntulenme_bu_ay.satis_sayi >= 9) and (canvesser_maas_goruntulenme_bu_ay.satis_sayi <= 14):
                satis_sayina_gore_prim = canvesser_prim.satis9_14
            elif (canvesser_maas_goruntulenme_bu_ay.satis_sayi >= 15):
                satis_sayina_gore_prim = canvesser_prim.satis15p
            elif (canvesser_maas_goruntulenme_bu_ay.satis_sayi >= 20):
                satis_sayina_gore_prim = canvesser_prim.satis20p

            canvesser_maas_goruntulenme_novbeti_ay.yekun_maas = float(canvesser_maas_goruntulenme_novbeti_ay.yekun_maas) + (float(canvesser_prim.komandaya_gore_prim) * float(instance.mehsul_sayi)) + float(satis_sayina_gore_prim)
            print(f"{canvesser_maas_goruntulenme_novbeti_ay.yekun_maas=}")

            canvesser_maas_goruntulenme_novbeti_ay.save()

        
        canvesserVezife = Vezifeler.objects.get(vezife_adi="CANVASSER")
        print(f"{canvesserVezife=}")
        canvessers = User.objects.filter(ofis=ofis, vezife=canvesserVezife)
        print(f"{canvessers=}")

        for canvesser in canvessers:
            canvesser_status = canvesser.isci_status
            print(f"{canvesser_status=}")
            canvesser_prim = CanvasserPrim.objects.get(prim_status=canvesser_status)
            print(f"{canvesser_prim=}")

            canvesser_maas_goruntulenme_novbeti_ay = MaasGoruntuleme.objects.get(isci=canvesser, tarix=next_m)
            print(f"{canvesser_maas_goruntulenme_novbeti_ay=}")

            canvesser_maas_goruntulenme_novbeti_ay.yekun_maas = float(canvesser_maas_goruntulenme_novbeti_ay.yekun_maas) + (float(canvesser_prim.ofise_gore_prim) * float(instance.mehsul_sayi))
            print(f"{canvesser_maas_goruntulenme_novbeti_ay.yekun_maas=}")

            canvesser_maas_goruntulenme_novbeti_ay.save()