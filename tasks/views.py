from django.shortcuts import render

from tasks.models import Task
from rest_framework.views import View, APIView
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from django.shortcuts import get_object_or_404


class TaskAPIView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            body = serializer.validated_data.get('body')
            estimated_finish_time = serializer.validated_data.get('estimated_finish_time')
            task = Task.objects.create(body=body, estimated_finish_time=estimated_finish_time)
            serializer = TaskSerializer(instance=task)
            return Response(serializer.data)

        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            body = serializer.validated_data.get('body')
            est = serializer.validated_data.get('estimated_finish_time')
            task.body = body
            task.estimated_finish_time = est
            task.save()
            return Response(serializer.data)

        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({'detail': 'success'}, status=status.HTT_204_NO_CONTENT)