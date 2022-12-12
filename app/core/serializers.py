from rest_framework import serializers
from core.models import Item
from core.api_utils import get_status_description, get_image_json


class ItemSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'number', 'status', 'image')

    def get_status(self, item):
        return get_status_description(item.status)

    def get_image(self, item):
        return get_image_json(item)
