
from django.urls import path
from users.userworkplace import views


urlpatterns = [
    path('user-workplace/', (views.create_user_workplace), name='create_user_workplace'),
]