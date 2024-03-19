from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
import json
from .models import role, permission, RolePermission, User ,userPermission
from rest_framework import viewsets
from .serializers import permissionSerializers, roleSerializers, RolePermissionSerializer,userPermissionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from users.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = role.objects.all()
    serializer_class = roleSerializers


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permission.objects.all()
    serializer_class = permissionSerializers


class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class userPermissionViewSet(viewsets.ModelViewSet):
    queryset = userPermission.objects.all()
    serializer_class = userPermissionSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = role.objects.all()
    serializer_class = roleSerializers


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = permission.objects.all()
    serializer_class = permissionSerializers


class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer

class userPermissionViewSet(viewsets.ModelViewSet):
    queryset = userPermission.objects.all()
    serializer_class = userPermissionSerializer

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


@csrf_exempt 
@permission_classes([IsAuthenticated]) 
def delete_user_by_id_role(request, user_id):
    
    user = get_object_or_404(role, role_id=user_id)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_user_by_id_role(request, user_id):
    user = get_object_or_404(role, role_id=user_id)
    serialized_user = roleSerializers(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_user_role(request):
    users = role.objects.all()
    serialized_users = roleSerializers(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})


@csrf_exempt
def update_user_by_id_role(request, user_id):
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
def delete_user_by_id_permission(request, user_id):
    user = get_object_or_404(permission, permission_id=user_id)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_user_by_id_permission(request, user_id):
    user = get_object_or_404(permission, id=user_id)
    serialized_user = permissionSerializers(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_user_permission(request):
    users = permission.objects.all()
    serialized_users = permissionSerializers(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})


@csrf_exempt
def update_user_by_id_permission(request, user_id):
    if request.method == 'PUT':
        try:
            users = permission.objects.get(id=user_id)
            data = json.loads(request.body.decode('utf-8'))
            # Update user attributes based on data received in the PUT request
            users.permission_name = data.get('permission_name', users.permission_name)
            users.description = data.get('description', users.description)
            
            users.save()
            return JsonResponse({'success': True, 'message': 'User updated successfully'})
        except role.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])  
@csrf_exempt
@api_view(['POST'])
def create_user(request):
    
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return JsonResponse({'message': 'Invalid content type'}, status=400)

        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode and parse JSON data

            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('user_name')
            password = data.get('password')
            email = data.get('email')
            if not (first_name and last_name and username and password and email):
                return JsonResponse({'message': 'All fields are required'}, status=400)

            hashed_password = make_password(password)
            role_id = 4
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_name=username,
                password=hashed_password,
                email=email,
                role_id=role_id
            )

            user_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_name': user.user_name,
                'email': user.email,
                'role_id': role_id
            }
            return JsonResponse({'message': 'User created successfully', 'data': user_data}, status=201)
        except (ValueError, Exception) as e:
            print(e)
            return JsonResponse({'message': 'Internal server error'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)

@api_view(['POST'])  
def superadmin(request):
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return JsonResponse({'message': 'Invalid content type'}, status=400)

        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode and parse JSON data

            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('user_name')
            password = data.get('password')
            email = data.get('email')
            if not (first_name and last_name and username and password and email):
                return JsonResponse({'message': 'All fields are required'}, status=400)

            hashed_password = make_password(password)
            role_id = 1
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                user_name=username,    
                password=hashed_password,
                email=email,
                role_id=role_id
            )
            user_data = {
                # 'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_name': user.user_name,
                'email': user.email,
                'role_id': user.role_id
            }
            return JsonResponse({'message': 'User created successfully', 'data': user_data}, status=201)
        except (ValueError, Exception) as e:
            print(e)
            return JsonResponse({'message': 'Internal server error'}, status=500)

    return JsonResponse({'message': 'Method not allowed'}, status=405)


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

def get_tokens_for_user(user_id):
    user = User.objects.get(id=user_id)
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    password = serializers.CharField()

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data.get('user_name')
            password = serializer.validated_data.get('password')
            
            try:
                user = User.objects.get(user_name=username)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=400)

            # Check if the provided password matches the user's password
            if check_password(password, user.password):
                user_id = user.id
                token = get_tokens_for_user(user_id)
                return Response({'token': token, 'user_id': user_id, 'message': 'Login successful'})
            else:
                return Response({'error': 'Invalid username or password'}, status=400)

        return Response(serializer.errors, status=400)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  
def test_token(request):
    return Response("passed {}".format(request.user.id))


