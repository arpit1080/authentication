from django.urls import path
from users.role import views


urlpatterns = [
    path('role/', (views.create_role), name='create_role'),

    path('getalldata_id_role/<int:user_id>/', (views.get_role), name='get_user_by_id_role'),

    path('getalldata_role/', (views.get_all_role), name='get_all_user_role'),

    path('deletealldata_id_role/<int:user_id>/', (views.delete_role), name='delete_user_by_id_role'),

    path('updatealldata_id_role/<int:user_id>/', (views.update_role), name='update_user_by_id_role'),
]