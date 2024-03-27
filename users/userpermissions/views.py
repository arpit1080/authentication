from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json
from .models import userPermission
from rest_framework import viewsets
from .serializers import userPermissionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers
from users.isauthorized import is_authorized





@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('create-user-permission')
@csrf_exempt
# @is_authorized(permission_name="create_user_permission")
def create_user_permission(request):
    if request.method == 'POST':
        try:
            # Parse request data
            data = json.loads(request.body)
            
            # Extract user_id from request data
            user_id = data.get('user_id')
            permission_id = data.get('permission_id')
            
            # Check if user_id and permission_id are provided
            if user_id is None or permission_id is None:
                return JsonResponse({'error': 'user_id and permission_id are required'}, status=400)
            
            # Create user permission
            user_permission = userPermission.objects.create(user_id=user_id, permission_id=permission_id)
            
            return JsonResponse({'success': True, 'message': 'User permission created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('delete-user-permission')
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def delete_userpermission(request, id):
    userPermission_obj = get_object_or_404(userPermission, id=id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the user as deleted
            userPermission_obj.deleted = True
            userPermission_obj.save()
            return JsonResponse({'success': True, 'message': 'rolepermission soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the user from the database
            userPermission_obj.delete()
            return JsonResponse({'success': True, 'message': 'rolepermission hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore workplace
            userPermission_obj.deleted = False
            userPermission_obj.save()
            return JsonResponse({'success': True, 'message': 'rolepermission restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-user-permission')
def get_userpermission(request, id):
    user = get_object_or_404(userPermission, id=id)
    serialized_user = userPermissionSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-all-user-permission')
def get_all_userpermission(request):
    users = userPermission.objects.all()
    serialized_users = userPermissionSerializer(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('update-user-permission')
@csrf_exempt
def update_userpermission(request, id):
    if request.method == 'PUT':
        try:
            user = userPermission.objects.get(id=id)
            data = json.loads(request.body.decode('utf-8'))
            user.user_id = data.get('user_id', user.user_id)
            user.permission_id = data.get('permission_id', user.permission_id)
            user.save()
            return JsonResponse({'success': True, 'message': 'userpermission updated successfully'})
        except userPermission.DoesNotExist:
            return JsonResponse({'error': 'userpermission not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


