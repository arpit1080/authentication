import jwt
from django.http import JsonResponse
from django.http import HttpRequest  # Import HttpRequest
from django.conf import settings

def verify_token_middleware(get_response):
    def middleware(request):
        # Ensure request is an instance of HttpRequest
        if not isinstance(request, HttpRequest):
            return JsonResponse({'message': 'Invalid request'}, status=400)

        token = request.headers.get('auth-token')
        if not token:
            return JsonResponse({'message': 'No token provided'}, status=403)

        try:
            
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = data.get('user')
            print(request.user_id)
            return get_response(request)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'Failed to authenticate token'}, status=401)

    return middleware

