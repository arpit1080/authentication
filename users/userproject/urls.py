
from django.urls import path
from users.userproject import views


urlpatterns = [
    path('user-project/', (views.create_user_project), name='create_user_project'),
]