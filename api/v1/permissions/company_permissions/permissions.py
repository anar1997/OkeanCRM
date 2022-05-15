from rest_framework import permissions
from api.v1.permissions.utils.permission_utils import PermissionUtil


class HoldingPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket", view=view)
        return perm_util.add_user_permission_to_list()

class OfisPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis", view=view)
        return perm_util.add_user_permission_to_list()

class ShobePermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shobe", view=view)
        return perm_util.add_user_permission_to_list()

class VezifelerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="vezifeler", view=view)
        return perm_util.add_user_permission_to_list()

class KomandaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="komanda", view=view)
        return perm_util.add_user_permission_to_list()

class OfisKassaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis_kassa", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket_kassa", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding_kassa", view=view)
        return perm_util.add_user_permission_to_list()

class OfisdenShirketeTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofisden_shirkete_transfer", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketdenOfislereTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketden_ofislere_transfer", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketdenHoldingeTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketden_holdinge_transfer", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingdenShirketlereTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holdingden_shirketlere_transfer", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding_kassa_medaxil", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holding_kassa_mexaric", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket_kassa_medaxil", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirket_kassa_mexaric", view=view)
        return perm_util.add_user_permission_to_list()

class OfisKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis_kassa_medaxil", view=view)
        return perm_util.add_user_permission_to_list()

class OfisKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofis_kassa_mexaric", view=view)
        return perm_util.add_user_permission_to_list()