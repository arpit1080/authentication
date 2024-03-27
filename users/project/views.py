
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import project
from rest_framework import viewsets
from .serializers import projectSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404




class projectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer




@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = projectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'project created successfully'})
        return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)





@csrf_exempt
def delete_project(request, project_id):
    project_obj = get_object_or_404(project, project_id=project_id)
    
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        
        # Check if 'delete_type' is specified in the request data
        delete_type = data.get('delete_type')

        if delete_type == 'soft':
            # Soft delete: Just mark the project as deleted
            project_obj.deleted = True
            project_obj.save()
            return JsonResponse({'success': True, 'message': 'Project soft deleted successfully'})

        elif delete_type == 'hard':
            # Hard delete: Remove the project from the database
            project_obj.delete()
            return JsonResponse({'success': True, 'message': 'Project hard deleted successfully'})

        else:
            return JsonResponse({'error': 'Invalid delete type'}, status=400)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        restore_action = data.get('restore')

        if restore_action == 'true':
            # Restore project
            project_obj.deleted = False
            project_obj.save()
            return JsonResponse({'success': True, 'message': 'Project restored successfully'})

        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)




def get_project(request, project_id):
    user = get_object_or_404(project, project_id=project_id)
    serialized_user = projectSerializer(user)
    return JsonResponse({'success': True, 'user': serialized_user.data})


def get_all_project(request):
    user = project.objects.all()
    serialized_users = projectSerializer(user, many=True)
    return JsonResponse({'success': True, 'users': serialized_users.data})



@csrf_exempt
def update_project(request, project_id):
    if request.method == 'PUT':
        try:
            user = project.objects.get(project_id=project_id)
            data = json.loads(request.body.decode('utf-8'))
            user.project_name = data.get('project_name', user.project_name)
            user.description = data.get('description', user.description)
            user.startdate = data.get('startdate',user.startdate)
            user.enddate = data.get('enddate',user.enddate)
            user.projecmanager = data.get('projecmanager',user.projecmanager)
            user.status = data.get('status',user.status)
            user.save()
            return JsonResponse({'success': True, 'message': 'project updated successfully'})
        except project.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


