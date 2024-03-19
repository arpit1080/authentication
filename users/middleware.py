from django.http import JsonResponse
from .models import User, role, permission, userPermission
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
from django.shortcuts import get_object_or_404


@csrf_exempt
def is_authorized(permission_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            print("Request user:", request)
            print("is_authorized called with request:", request)
            if not request.user.is_authenticated:
                print("Request user:", request.user.id)
                return JsonResponse({"error": "Authentication required."}, status=401)

            try:
                user = get_object_or_404(User, id=request.user.id)
                user_roles = user.roles.all()
                role_permissions = permission.objects.filter(role__in=user_roles, permission_name=permission_name)

                if role_permissions.exists():
                    user_permission = userPermission.objects.filter(user=user, permission__permission_name=permission_name)
                    if user_permission.exists():
                        print("User ID:", user.id)
                        print("User has permission for", permission_name)
                        return view_func(request, *args, **kwargs)
                    else:
                        return JsonResponse({"error": f"Access forbidden. You do not have permission to access {permission_name}."}, status=403)
                else:
                    return JsonResponse({"error": f"Access forbidden. No role has permission for {permission_name}."}, status=403)
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found."}, status=404)
            except permission.DoesNotExist:
                return JsonResponse({"error": f"No permission named {permission_name}."}, status=404)
            except Exception as e:
                print("Error:", e)
                return JsonResponse({"error": "Internal server error."}, status=500)
        return wrapped_view
    return decorator
