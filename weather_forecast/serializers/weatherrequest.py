from rest_framework import serializers

class WeatherRequestSerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True, error_messages={'required': 'O campo "lat" é obrigatório.'})
    lon = serializers.FloatField(required=True, error_messages={'required': 'O campo "lon" é obrigatório.'})
