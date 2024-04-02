from rest_framework import serializers
from .models import Moovie

class MoovieSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Moovie
        fields = '__all__'
