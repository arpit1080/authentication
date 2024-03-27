from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import json
from .models import userproject
from rest_framework import viewsets
from .serializers import userprojectSerializer
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

class userprojectViewSet(viewsets.ModelViewSet):
    queryset = userproject.objects.all()
    serializer_class =userprojectSerializer



# @authentication_classes([TokenAuthentication,SessionAuthentication])
# @permission_classes([IsAuthenticated])  
# @csrf_exempt
# @is_authorized('create-role-permission')
# @csrf_exempt
# @is_authorized(permission_name="create_user_permission")
def create_user_project(request):
    if request.method == 'POST':
        try:
            # Parse request data
            data = json.loads(request.body)
            
            # Extract user_id from request data
            user_id = data.get('user_id')
            project_id = data.get('project_id')
            
            # Check if user_id and permission_id are provided
            if user_id is None or project_id is None:
                return JsonResponse({'error': 'user_id and project_id are required'}, status=400)
            
            # Create user permission
            user_project = userproject.objects.create(user_id=user_id, project_id=project_id)
            
            return JsonResponse({'success': True, 'message': 'user-project created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
