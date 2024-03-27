
from django.urls import path
from users.rolepermissions import views


urlpatterns = [
    path('role-permissions/', (views.create_role_permission), name='create_role_permission'),

    path('getalldata_id_rolepermission/<int:user_id>/', (views.get_rolepermission), name='get_rolepermission'),

    path('getalldata_rolepermission/', (views.get_all_rolepermission), name='get_all_rolepermission'),

    path('deletealldata_id_rolepermission/<int:user_id>/', (views.delete_rolepermission), name='delete_rolepermission'),

    path('updatealldata_id_rolepermission/<int:user_id>/', (views.update_rolepermission), name='update_rolepermission'),

]
