from rest_framework import serializers

class CVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
