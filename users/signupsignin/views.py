from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import serializers
from users.isauthorized import is_authorized

# @authentication_classes([TokenAuthentication,SessionAuthentication])
# @permission_classes([IsAuthenticated])  
# @csrf_exempt
# @is_authorized('create-user')
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


def get_tokens_for_user(user):
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
            user_name = serializer.validated_data.get('user_name')
            password = serializer.validated_data.get('password')
            
            try:
                user = User.objects.get(user_name=user_name)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=400)

            # Check if the provided password matches the user's password
            if check_password(password, user.password):
                token = get_tokens_for_user(user)
                print(user.user_id)
                # return tokens along with user data
                return Response({'token': token, 'user': {'user_name': user.user_name, 'email': user.email}, 'message': 'Login successful'})
            else:
                return Response({'error': 'Invalid username or password'}, status=400)

        return Response(serializer.errors, status=400)

