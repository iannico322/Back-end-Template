from rest_framework.permissions import BasePermission


def is_admin_user(user) -> bool:
    """
    True for Django superusers and for users with acc_lvl == 0 — the app's
    own "admin" tier that also gates the React admin panel.
    """
    return bool(
        user
        and user.is_authenticated
        and (user.is_superuser or getattr(user, "acc_lvl", None) == 0)
    )


class IsAccLevelAdmin(BasePermission):
    def has_permission(self, request, view):
        return is_admin_user(request.user)
