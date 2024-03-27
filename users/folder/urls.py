from django.urls import path
from . import views
from users.folder import views

urlpatterns = [
   
    path('folder/', views.create_folder, name='create_folder'),
    path('get_folder/<int:folder_id>/', views.get_folder, name='get_folder'),
    path('get_all_folder/', views.get_all_folder, name='get_all_folder'),
    path('delete_folder/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('update_folder/<int:folder_id>/', views.update_folder, name='update_folder'),

]