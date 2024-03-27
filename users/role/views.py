from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json
from .models import role
from rest_framework import viewsets
from .serializers import  roleSerializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers
from users.isauthorized import is_authorized





class roleViewSet(viewsets.ModelViewSet):
    queryset = role.objects.all()
    serializer_class = roleSerializers


@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('create-role')
@csrf_exempt
def create_role(request):
    
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = roleSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Role created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('delete-role')
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def delete_role(request, role_id):
    role_obj = get_object_or_404(role, role_id=role_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the user as deleted
            role_obj.deleted = True
            role_obj.save()
            return JsonResponse({'success': True, 'message': 'role soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the user from the database
            role_obj.delete()
            return JsonResponse({'success': True, 'message': 'role hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore workplace
            role_obj.deleted = False
            role_obj.save()
            return JsonResponse({'success': True, 'message': 'Workplace restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-role')
def get_role(request, user_id):
    user = get_object_or_404(role, role_id=user_id)
    serialized_user = roleSerializers(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('get-all-role')
def get_all_role(request):
    users = role.objects.all()
    serialized_users = roleSerializers(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})




@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@is_authorized('update-role')
@csrf_exempt
def update_role(request, user_id):
    if request.method == 'PUT':
        try:
            user = role.objects.get(id=user_id)
            data = json.loads(request.body.decode('utf-8'))
            user.role_name = data.get('role_name', user.role_name)
            user.save()
            return JsonResponse({'success': True, 'message': 'User updated successfully'})
        except role.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


