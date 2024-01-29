from rest_framework import serializers

from api.models import Package


class VideoColorSerializer(serializers.Serializer):
    brightness = serializers.IntegerField(min_value=0, max_value=100)
    contrast = serializers.IntegerField(min_value=0, max_value=100)
    hue = serializers.IntegerField(min_value=0, max_value=100)
    saturation = serializers.IntegerField(min_value=0, max_value=100)


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

    def save(self, *args, **kwargs):
        video_color = self.validated_data["video_color"]
        serializer = VideoColorSerializer(data=video_color)
        serializer.is_valid(raise_exception=True)
        return Package.objects.create(**self.validated_data)
