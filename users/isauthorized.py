from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User, role, permission, RolePermission, userPermission

def is_authorized(permissions_enum):
    def middleware(get_response):
        def wrapper(request):
            user_id = getattr(request, 'user_id', None)  # Get user_id from request
            print(user_id)
            if user_id is None:
                return JsonResponse({'error': 'User ID not found in request'}, status=403)
            
            try:
                # Find the user by primary key
                user = get_object_or_404(User, user_id=user_id)
                print(user.user_id)
                # Fetch the role associated with the user
                role_instance = get_object_or_404(role, role_id=user.role_id)
                print(role_instance.role_id)
                # Fetch all permissions associated with the user's role
                role_permissions = RolePermission.objects.filter(role_id=user.role_id).values_list('permission_id', flat=True)
                print(role_permissions)
                # Fetch the permission corresponding to the permissionsEnum
                permission_instance = get_object_or_404(permission, permission_name=permissions_enum)
                print(permissions_enum)
                # Check if the permission you're looking for is among the user's permissions
                if permission_instance.permission_id in role_permissions:
                    # Check if the permission is assigned to the user in the userPermission table
                    user_permission = userPermission.objects.filter(user_id=user.user_id, permission_id=permission_instance.permission_id).exists()
                    if user_permission:
                        print("User has permission:", permissions_enum)
                        return get_response(request)  # Pass request to next middleware or view
                    else:
                        return JsonResponse({"error": "Access denied. You do not have permission to access this resource."}, status=403)
                else:
                    return JsonResponse({"error": f"Access denied. You do not have permission to access this resource: {permissions_enum}"}, status=403)

            except User.DoesNotExist:
                return JsonResponse({"error": "User not found. Please check your credentials."}, status=404)
            except role.DoesNotExist:
                return JsonResponse({"error": "No role found for this user."}, status=403)
            except permission.DoesNotExist:
                return JsonResponse({"error": f"Permission not found: {permissions_enum}"}, status=403)
            except Exception as e:
                print('Error occurred:', e)
                return JsonResponse({"error": "Oops! Something went wrong. Please try again later."}, status=500)

        return wrapper

    return middleware
