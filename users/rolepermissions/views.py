from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json
from .models import RolePermission
from rest_framework import viewsets
from .serializers import RolePermissionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404 
from django.contrib.auth.hashers import make_password
from users.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers
from users.isauthorized import is_authorized
from rest_framework.viewsets import ModelViewSet
from .models import RolePermission
from .serializers import RolePermissionSerializer

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer



@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('create-role-permission')
@csrf_exempt
# @is_authorized(permission_name="create_user_permission")
def create_role_permission(request):
    if request.method == 'POST':
        try:
            # Parse request data
            data = json.loads(request.body)
            
            # Extract user_id from request data
            role_id = data.get('role_id')
            permission_id = data.get('permission_id')
            
            # Check if user_id and permission_id are provided
            if role_id is None or permission_id is None:
                return JsonResponse({'error': 'role_id and permission_id are required'}, status=400)
            
            # Create user permission
            user_permission = RolePermission.objects.create(role_id=role_id, permission_id=permission_id)
            
            return JsonResponse({'success': True, 'message': 'role permission created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('delete-role-permission')
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def delete_rolepermission(request, id):
    rolepermission_obj = get_object_or_404(RolePermission, id=id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the user as deleted
            rolepermission_obj.deleted = True
            rolepermission_obj.save()
            return JsonResponse({'success': True, 'message': 'rolepermission soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the user from the database
            rolepermission_obj.delete()
            return JsonResponse({'success': True, 'message': 'rolepermission hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore workplace
            rolepermission_obj.deleted = False
            rolepermission_obj.save()
            return JsonResponse({'success': True, 'message': 'rolepermission restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-role-permission')
def get_rolepermission(request, id):
    user = get_object_or_404(RolePermission, id=id)
    serialized_user = RolePermissionSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-all-role-permission')
def get_all_rolepermission(request):
    users = RolePermission.objects.all()
    serialized_users = RolePermissionSerializer(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('update-role-permission')
@csrf_exempt
def update_rolepermission(request, id):
    if request.method == 'PUT':
        try:
            user = RolePermission.objects.get(id=id)
            data = json.loads(request.body.decode('utf-8'))
            user.role_id = data.get('role_id', user.role_id)
            user.permission_id = data.get('permission_id', user.permission_id)
            user.save()
            return JsonResponse({'success': True, 'message': 'rolepermission updated successfully'})
        except RolePermission.DoesNotExist:
            return JsonResponse({'error': 'rolepermission not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


