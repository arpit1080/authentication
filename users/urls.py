from django.urls import path, include
from users.permission import urls
from users.role import urls
from users.rolepermissions import urls
from users.userpermissions import urls
from users.signupsignin import urls
from users.projectuser import urls
from users.userproject import urls
from users.userworkplace import urls



urlpatterns = [
    path('role/', include("users.role.urls")),
    path('permission/', include("users.permission.urls")),
    path('role_permission/', include("users.rolepermissions.urls")),
    path('signup-signin/', include("users.signupsignin.urls")),
    path('user-permission/', include("users.userpermissions.urls")),
    path('workplace/', include("users.workplace.urls")),
    path('project/', include("users.project.urls")),
    path('folder/', include("users.folder.urls")),
    path('subfolder/', include("users.subfolder.urls")),
    path('projectuser/', include("users.projectuser.urls")),
    path('userproject/', include("users.userproject.urls")),
    path('workplaceproject/', include("users.workplaceproject.urls")),
    path('userworkplace/', include("users.userworkplace.urls")),
]





