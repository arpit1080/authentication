from django.urls import path
from users.signupsignin import views
from users.middleware import verify_token_middleware

urlpatterns = [
    path("login/", views.user_login, name='user_login'),
    path("user/",(views.create_user), name='create_user'),
    path("superadmin/", views.superadmin, name='superadmin'),
]