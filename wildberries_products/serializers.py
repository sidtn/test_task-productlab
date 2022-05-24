from rest_framework.serializers import FileField, Serializer


class UploadExelSerializer(Serializer):
    file = FileField()

    class Meta:
        fields = ["file"]
