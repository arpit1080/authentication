from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import folder
from rest_framework import viewsets
from .serializers import folderSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404



class folderViewSet(viewsets.ModelViewSet):
    queryset = folder.objects.all()
    serializer_class = folderSerializer

@csrf_exempt
def create_folder(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = folderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'folder created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt
def delete_folder(request, folder_id):
    folder_obj = get_object_or_404(folder, folder_id=folder_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the folder as deleted
            folder_obj.deleted = True
            folder_obj.save()
            return JsonResponse({'success': True, 'message': 'Folder soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the folder from the database
            folder_obj.delete()
            return JsonResponse({'success': True, 'message': 'Folder hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore folder
            folder_obj.deleted = False
            folder_obj.save()
            return JsonResponse({'success': True, 'message': 'Folder restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_folder(request, folder_id):
    user = get_object_or_404(folder, folder_id=folder_id)
    serialized_user = folderSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_folder(request):
    user = folder.objects.all()
    serialized_users = folderSerializer(user, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})



@csrf_exempt
def update_folder(request, folder_id):
    if request.method == 'PUT':
        try:
            user = folder.objects.get(folder_id=folder_id)
            data = json.loads(request.body.decode('utf-8'))
            user.folder_name = data.get('folder_name', user.folder_name)
            user.description = data.get('description', user.description)
           
            return JsonResponse({'success': True, 'message': 'folder updated successfully'})
        except folder.DoesNotExist:
            return JsonResponse({'error': 'folder not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



