# from rest_framework.exceptions import ValidationError
# from django.shortcuts import get_object_or_404
# from company.models import OfisKassa, OfisKassaMedaxil
# from mehsullar.models import Muqavile
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import datetime
# import traceback
#
# @receiver(post_save, sender=Muqavile)
# def create_ofis_kassa_medaxil(sender, instance, created, **kwargs):
#     if created:
#         print("create_ofis_kassa_medaxil")
#         vanleader = instance.vanleader
#         print(f"vanleader ==> {vanleader}")
#         ofis = vanleader.ofis
#         print(f"ofis ==> {ofis}")
#
#         mebleg = instance.muqavile_umumi_mebleg
#         print(f"mebleg ==> {mebleg}")
#
#         tarix = instance.muqavile_tarixi
#         print(f"tarix ==> {tarix}")
#
#         qeyd = f"{instance} müqaviləsi imzalandığı üçün {ofis} ofisinə {mebleg} azn mədaxil edildi"
#
#         try:
#             ofis_kassa = get_object_or_404(OfisKassa, ofis=ofis)
#             print(f"ofis_kassa ==> {ofis_kassa}")
#             medaxil = OfisKassaMedaxil.objects.create(
#                 medaxil_eden = vanleader,
#                 ofis_kassa=ofis_kassa,
#                 mebleg=mebleg,
#                 medaxil_tarixi=tarix,
#                 qeyd = qeyd
#             )
#             medaxil.save()
#         except Exception:
#             traceback.print_exc()
#