
from django.urls import path
from users.projectuser import views


urlpatterns = [
    path('project-user/', (views.create_project_user), name='create_project_user'),
]