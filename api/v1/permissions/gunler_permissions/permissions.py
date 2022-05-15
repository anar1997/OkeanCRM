from rest_framework import permissions
from api.v1.permissions.utils.permission_utils import PermissionUtil

# class IstisnaIsciPermissions(permissions.IsAdminUser):
#     def has_permission(self, request, view):
#         perm_util = PermissionUtil(user=request.user, request=request, object_name="istisna_isci", view=view)
#         return perm_util.add_user_permission_to_list()
       
class IsciGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="isci_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class OfisGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class KomandaGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="komanda_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class VezifeGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="vezife_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class ShobeGunlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shobe_gunler", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()

class OfisIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()

class ShobeIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shobe_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()

class KomandaIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="komanda_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()

class VezifeIstisnaIsciPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="vezife_istisna_isci", view=view)
        return perm_util.add_user_permission_to_list()
