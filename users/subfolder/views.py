from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import subfolder
from rest_framework import viewsets
from .serializers import subfolderSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



class subfolderViewSet(viewsets.ModelViewSet):
    queryset = subfolder.objects.all()
    serializer_class = subfolderSerializer



@csrf_exempt
def create_subfolder(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = subfolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'subfolder created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt
def delete_subfolder(request, subfolder_id):
    subfolder_obj = get_object_or_404(subfolder, subfolder_id=subfolder_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the subfolder as deleted
            subfolder_obj.deleted = True
            subfolder_obj.save()
            return JsonResponse({'success': True, 'message': 'Subfolder soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the subfolder from the database
            subfolder_obj.delete()
            return JsonResponse({'success': True, 'message': 'Subfolder hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore subfolder
            subfolder_obj.deleted = False
            subfolder_obj.save()
            return JsonResponse({'success': True, 'message': 'Subfolder restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)





def get_subfolder(request, subfolder_id):
    user = get_object_or_404(subfolder, subfolder_id=subfolder_id)
    serialized_user = subfolderSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_subfolder(request):
    user = subfolder.objects.all()
    serialized_users = subfolderSerializer(user, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})



@csrf_exempt
def update_subfolder(request, subfolder_id):
    if request.method == 'PUT':
        try:
            user = subfolder.objects.get(subfolder_id=subfolder_id)
            data = json.loads(request.body.decode('utf-8'))
            user.subfolder_name = data.get('subfolder_name', user.subfolder_name)
            user.description = data.get('description', user.description)
           
            return JsonResponse({'success': True, 'message': 'subfolder updated successfully'})
        except subfolder.DoesNotExist:
            return JsonResponse({'error': 'subfolder not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

