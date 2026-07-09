from .models import AfricaCountry
from rest_framework import serializers

class AfricaCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AfricaCountry
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AfricaCountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfricaCountry
        fields = ['id', 'name', 'capital', 'population', 'area', 'currency', 'official_language']

        read_only_fields = ['id']
        