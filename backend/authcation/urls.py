from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.user_login, name='user_login'),
]
