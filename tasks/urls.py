from django.urls import path
from tasks.views import TaskAPIView, TaskDetailAPIView
urlpatterns = [
    path('tasks/',  TaskAPIView.as_view(), name='tasks_list_url'),
    path('tasks/<int:id>/',  TaskDetailAPIView.as_view(), name='task_detail_url'),
]