from rest_framework import serializers
from .models import Rock


class RockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('owner', 'name', 'description', 'time_stamp_creation')
        model = Rock
