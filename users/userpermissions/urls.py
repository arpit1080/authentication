
from django.urls import path
from users.userpermissions import views


urlpatterns = [
    path('user-permission/', (views.create_user_permission), name='create_user_permission'),

    path('getalldata_id_userpermission/<int:user_id>/', (views.get_userpermission), name='get_userpermission'),

    path('getalldata_userpermission/', (views.get_all_userpermission), name='get_all_userpermission'),

    path('deletealldata_id_userpermission/<int:user_id>/', (views.delete_userpermission), name='delete_userpermission'),

    path('updatealldata_id_userpermission/<int:user_id>/', (views.update_userpermission), name='update_userpermission'),

]