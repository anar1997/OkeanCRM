from rest_framework import permissions
from api.v1.permissions.utils.permission_utils import PermissionUtil


class UserPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="user", view=view)
        return perm_util.add_user_permission_to_list()

class IsciStatusPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="isci_status", view=view)
        return perm_util.add_user_permission_to_list()

class BolgePermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="bolge", view=view)
        return perm_util.add_user_permission_to_list()

class MusteriPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="musteri", view=view)
        return perm_util.add_user_permission_to_list()

class MusteriQeydlerPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="musteri_qeydler", view=view)
        return perm_util.add_user_permission_to_list()

class IsciSatisSayiPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="isci_satis_sayi", view=view)
        return perm_util.add_user_permission_to_list()