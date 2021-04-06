from rest_framework import serializers
from . models import Students

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'name', 'roll', 'city']
