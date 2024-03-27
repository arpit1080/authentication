from django.urls import path
from users.permission import views


urlpatterns = [
    path('permission/', (views.create_permission), name='create_permission'),

    path('getalldata_id_permission/<int:user_id>/', (views.get_permission), name='get_user_by_id_permission'),

    path('getalldata_permission/', (views.get_all_permission), name='get_all_user_permission'),

    path('deletealldata_id_permission/<int:user_id>/', (views.delete_permission), name='delete_user_by_id_permission'),

    path('updatealldata_id_permission/<int:user_id>/', (views.update_permission), name='update_user_by_id_permission'),
]