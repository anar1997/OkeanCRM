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
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofiskassa", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketkassa", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holdingkassa", view=view)
        return perm_util.add_user_permission_to_list()

class OfisdenShirketeTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofisdenshirketetransfer", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketdenOfislereTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketdenofisleretransfer", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketdenHoldingeTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketdenholdingetransfer", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingdenShirketlereTransferPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holdingdenshirketleretransfer", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holdingkassamedaxil", view=view)
        return perm_util.add_user_permission_to_list()

class HoldingKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="holdingkassamexaric", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketkassamedaxil", view=view)
        return perm_util.add_user_permission_to_list()

class ShirketKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="shirketkassamexaric", view=view)
        return perm_util.add_user_permission_to_list()

class OfisKassaMedaxilPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofiskassamedaxil", view=view)
        return perm_util.add_user_permission_to_list()

class OfisKassaMexaricPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="ofiskassamexaric", view=view)
        return perm_util.add_user_permission_to_list()