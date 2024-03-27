from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import workplace
from rest_framework import viewsets
from .serializers import workplaceSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

class workplaceViewSet(viewsets.ModelViewSet):
    queryset = workplace.objects.all()
    serializer_class = workplaceSerializer


@csrf_exempt
def create_workplace(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = workplaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'workplace created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt
def delete_workplace(request, workplace_id):
    workplace_obj = get_object_or_404(workplace, workplace_id=workplace_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the user as deleted
            workplace_obj.deleted = True
            workplace_obj.save()
            return JsonResponse({'success': True, 'message': 'Workplace soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the user from the database
            workplace_obj.delete()
            return JsonResponse({'success': True, 'message': 'Workplace hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore workplace
            workplace_obj.deleted = False
            workplace_obj.save()
            return JsonResponse({'success': True, 'message': 'Workplace restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)





def get_workplace(request, workplace_id):
    user = get_object_or_404(workplace, workplace_id=workplace_id)
    serialized_user = workplaceSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_workplace(request):
    users = workplace.objects.all()
    serialized_users = workplaceSerializer(users, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})



@csrf_exempt
def update_workplace(request, workplace_id):
    if request.method == 'PUT':
        try:
            user = workplace.objects.get(workplace_id=workplace_id)
            data = json.loads(request.body.decode('utf-8'))
            user.workplace_name = data.get('workplace_name', user.workplace_name)
            user.description = data.get('description', user.description)
            user.save()
            return JsonResponse({'success': True, 'message': 'User updated successfully'})
        except workplace.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


