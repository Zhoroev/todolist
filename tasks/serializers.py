from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    body = serializers.CharField()
    estimated_finish_time = serializers.DateTimeField(format="%d-%m-%Y %H-%M",
                                                      input_formats=['%d-%m-%Y %H-%M'])
    is_completed = serializers.BooleanField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True, format="%d-%m-%Y %H-%M")
