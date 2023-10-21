from django.urls import path, include
from rest_framework import routers

from .views import TaskViewSet, TaskCommentViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task-comments', TaskCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
