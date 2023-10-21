from rest_framework import viewsets
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCommentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_user=self.request.user)

class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
