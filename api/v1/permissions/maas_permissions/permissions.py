from rest_framework import permissions
from api.v1.permissions.utils.permission_utils import PermissionUtil
       
class VanLeaderPrimPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="vanLeader_prim", view=view)
        return perm_util.add_user_permission_to_list()

class DealerPrimPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="dealer_prim", view=view)
        return perm_util.add_user_permission_to_list()

class OfficeLeaderPrimPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="office_leader_prim", view=view)
        return perm_util.add_user_permission_to_list()

class CanvasserPrimPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="canvasser_prim", view=view)
        return perm_util.add_user_permission_to_list()

class AvansPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="avans", view=view)
        return perm_util.add_user_permission_to_list()

class KesintiPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="kesinti", view=view)
        return perm_util.add_user_permission_to_list()

class BonusPermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="bonus", view=view)
        return perm_util.add_user_permission_to_list()

class MaasGoruntulemePermissions(permissions.IsAdminUser):
    def has_permission(self, request, view):
        perm_util = PermissionUtil(user=request.user, request=request, object_name="maas_goruntuleme", view=view)
        return perm_util.add_user_permission_to_list()