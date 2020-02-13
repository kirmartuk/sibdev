from rest_framework import serializers
from .models import *


class DealSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer = serializers.CharField()
    item = serializers.CharField()
    total = serializers.IntegerField()
    quantity = serializers.IntegerField()
    date = serializers.CharField()

    def create(self, **data):
        return Deal.objects.create(**data)
