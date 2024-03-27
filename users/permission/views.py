from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json
from .models import  permission
from rest_framework import viewsets
from .serializers import permissionSerializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers
from users.isauthorized import is_authorized





class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permission.objects.all()
    serializer_class = permissionSerializers



# @authentication_classes([TokenAuthentication,SessionAuthentication])
# @permission_classes([IsAuthenticated])  
# @csrf_exempt
# @is_authorized('create-permission')
@csrf_exempt
def create_permission(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = permissionSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Permission created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt
def delete_permission(request, permission_id):
    permission_obj = get_object_or_404(permission, permission_id=permission_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the user as deleted
            permission_obj.deleted = True
            permission_obj.save()
            return JsonResponse({'success': True, 'message': 'permission soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the user from the database
            permission_obj.delete()
            return JsonResponse({'success': True, 'message': 'permission hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore workplace
            permission_obj.deleted = False
            permission_obj.save()
            return JsonResponse({'success': True, 'message': 'permission restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-permission')
def get_permission(request, user_id):
    user = get_object_or_404(permission, permission_id=user_id)
    serialized_user = permissionSerializers(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})



@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-all-permission')
def get_all_permission(request):
    users = permission.objects.all()
    serialized_users = permissionSerializers(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})


@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('update-permission')
@csrf_exempt
def update_permission(request, user_id):
    if request.method == 'PUT':
        try:
            users = permission.objects.get(id=user_id)
            data = json.loads(request.body.decode('utf-8'))
            # Update user attributes based on data received in the PUT request
            users.permission_name = data.get('permission_name', users.permission_name)
            users.description = data.get('description', users.description)
            
            users.save()
            return JsonResponse({'success': True, 'message': 'User updated successfully'})
        except permission.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


