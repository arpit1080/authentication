from django.urls import path
from users import views
from django.urls import path
from . import views
from users.middleware import is_authorized
from .views import RolePermissionViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'role-permission', RolePermissionViewSet, basename='role-permission')


schema_view = get_schema_view(
    openapi.Info(
        title="CRM",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
  

    path("login/", views.user_login, name='user_login'),

    path('role/',is_authorized (views.create_role), name='create_role'),

    path('getalldata_id_role/<int:user_id>/', is_authorized(views.get_user_by_id_role), name='get_user_by_id_role'),

    path('getalldata_role/',is_authorized (views.get_all_user_role), name='get_all_user_role'),

    path('deletealldata_id_role/<int:user_id>/',is_authorized (views.delete_user_by_id_role), name='delete_user_by_id_role'),

    path('updatealldata_id_role/<int:user_id>/',is_authorized (views.update_user_by_id_role), name='update_user_by_id_role'),

    path('permission/', is_authorized(views.create_permission), name='create_permission'),

    path('getalldata_id_permission/<int:user_id>/', is_authorized(views.get_user_by_id_permission), name='get_user_by_id_permission'),

    path('getalldata_permission/', is_authorized(views.get_all_user_permission), name='get_all_user_permission'),

    path('deletealldata_id_permission/<int:user_id>/', is_authorized(views.delete_user_by_id_permission), name='delete_user_by_id_permission'),

    path('updatealldata_id_permission/<int:user_id>/', is_authorized(views.update_user_by_id_permission), name='update_user_by_id_permission'),

    path('user-permission/', (views.create_user_permission), name='create_user_permission'),

    path("user/", is_authorized(views.create_user), name='create_user'),

    path("superadmin/", views.superadmin, name='superadmin'),
   
    path("test_token/", views.test_token, name='test_token'),



]




urlpatterns += router.urls
