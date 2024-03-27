from django.urls import path
from . import views
from users.workplace import views

urlpatterns = [
    
    path('workplace/', views.create_workplace, name='create_workplace'),
    path('get_workplace/<int:workplace_id>/', views.get_workplace, name='get_workplace'),
    path('get_all_workplace/', views.get_all_workplace, name='get_all_workplace'),
    path('delete_workplace/<int:workplace_id>/', views.delete_workplace, name='delete_workplace'),
    path('update_workplace/<int:workplace_id>/', views.update_workplace, name='update_workplace'),
]