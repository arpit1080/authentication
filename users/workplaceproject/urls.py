
from django.urls import path
from users.workplaceproject import views


urlpatterns = [
    path('workplace-project/', (views.create_workplace_project), name='create_workplace_project'),
]