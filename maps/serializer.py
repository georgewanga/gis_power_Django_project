from . rest_framework import serializers
from .models import Primary_substations

class Primary_substationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primary_substations
        #fields = ('geom')
        fields = '__all__'