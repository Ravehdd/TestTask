from rest_framework import serializers
from .models import *


class PurchaseSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    money = serializers.IntegerField()