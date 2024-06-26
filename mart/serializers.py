
from rest_framework import serializers

from . import models

class GenericProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'