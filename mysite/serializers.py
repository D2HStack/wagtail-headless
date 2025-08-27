from rest_framework import serializers


class RichTextSerializer(serializers.CharField):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return expand_db_html(representation)