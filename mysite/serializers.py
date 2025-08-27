from rest_framework import serializers

from wagtail.rich_text import expand_db_html
from wagtail.images.models import Image

from utils.models import ArticleTopic

class RichTextSerializer(serializers.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return expand_db_html(representation)
    
class CaptionedImageBlockSerializer(serializers.Serializer):
    image = serializers.SerializerMethodField()
    image_alt_text = serializers.CharField(required=False, allow_blank=True)
    caption = serializers.CharField(required=False, allow_blank=True)

    def get_image(self, obj):
        image_id = obj.get("image")
        if not image_id:
            return None
        try:
            image = Image.objects.get(id=image_id)
            return {
                "url": image.file.url,
                "alt": image.title,
                "width": image.width,
                "height": image.height,
            }
        except Image.DoesNotExist:
            return None

class ArticleTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTopic
        fields = ['id', 'title', 'slug']