from rest_framework.serializers import FileField, Serializer


class UploadExelSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ["exel_uploaded"]
