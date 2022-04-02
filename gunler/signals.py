# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from company.models import Holding, Komanda, Ofis, Shobe, Vezifeler
# from gunler.models import (
#     IsGunleri,
#     IsciGunler,
#     HoldingGunler,
#     KomandaGunler,
#     OfisGunler,
#     ShobeGunler,
#     VezifeGunler
# )
# from account.models import User

# @receiver(post_save, sender=IsGunleri)
# def create_isci_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         isciler = User.objects.all()
#         print(f"isciler ==> {isciler}")
#         for i in isciler:
#             IsciGunler.objects.create(
#                 isci = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()

# @receiver(post_save, sender=IsGunleri)
# def create_holding_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         holdingler = Holding.objects.all()
#         print(f"holdingler ==> {holdingler}")
#         for i in holdingler:
#             HoldingGunler.objects.create(
#                 holding = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()

# @receiver(post_save, sender=IsGunleri)
# def create_ofis_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         ofisler = Ofis.objects.all()
#         print(f"ofisler ==> {ofisler}")
#         for i in ofisler:
#             OfisGunler.objects.create(
#                 ofis = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()

# @receiver(post_save, sender=IsGunleri)
# def create_komanda_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         komandalar = Komanda.objects.all()
#         print(f"komandalar ==> {komandalar}")
#         for i in komandalar:
#             KomandaGunler.objects.create(
#                 komanda = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()

# @receiver(post_save, sender=IsGunleri)
# def create_shobe_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         shobeler = Shobe.objects.all()
#         print(f"shobeler ==> {shobeler}")
#         for i in shobeler:
#             ShobeGunler.objects.create(
#                 shobe = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()

# @receiver(post_save, sender=IsGunleri)
# def create_vezife_gunler(sender, instance, created, **kwargs):
#     if created:
#         print("create_gunler")
#         print(f"sender ==> {sender}")
#         print(f"instance ==> {instance}")
#         is_gunleri = instance.is_gunleri
#         print(f"is_gunleri ==> {is_gunleri}")
#         vezifeler = Vezifeler.objects.all()
#         print(f"vezifeler ==> {vezifeler}")
#         for i in vezifeler:
#             VezifeGunler.objects.create(
#                 vezife = i,
#                 is_gunleri = instance,
#                 tarix = instance.tarix
#             ).save()