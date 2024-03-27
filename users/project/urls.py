from django.urls import path
from . import views
from users.project import views



urlpatterns = [
   
    path('project/', views.create_project, name='create_project'),
    path('get_project/<int:project_id>/', views.get_project, name='get_project'),
    path('get_all_project/', views.get_all_project, name='get_all_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update_project/<int:project_id>/', views.update_project, name='update_project'),

]