from django.urls import path
from . import views
from users.subfolder import views

urlpatterns = [
   

    path('subfolder/', views.create_subfolder, name='create_subfolder'),
    path('get_subfolder/<int:subfolder_id>/', views.get_subfolder, name='get_subfolder'),
    path('get_all_subfolder/', views.get_all_subfolder, name='get_all_subfolder'),
    path('delete_subfolder/<int:subfolder_id>/', views.delete_subfolder, name='delete_subfolder'),
    path('update_subfolder/<int:subfolder_id>/', views.update_subfolder, name='update_subfolder'),

]
