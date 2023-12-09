from rest_framework import serializers
from datetime import datetime
from ..models import Temperature

class TemperatureSerializer(serializers.ModelSerializer):
    temperatura_celsius = serializers.SerializerMethodField()
    dia = serializers.SerializerMethodField()
    class Meta:
        model = Temperature
        fields = ["dia","temperatura_celsius"]

    def get_temperatura_celsius(self, obj):
        temperatura_kelvin = obj.day 
        temperatura_celsius = temperatura_kelvin - 273.15
        return round(temperatura_celsius, 2) if temperatura_celsius else None

    def get_dia(self, obj):
        data_timestamp = obj.dt
        data_formatada = datetime.fromtimestamp(data_timestamp).strftime('%d/%m/%Y')
        return data_formatada
        