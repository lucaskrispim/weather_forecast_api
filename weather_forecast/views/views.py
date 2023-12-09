from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Temperature
from ..serializers import TemperatureSerializer,WeatherRequestSerializer
from rest_framework import status
from ..forecast import get_weather_data
import datetime
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit

class TemperatureForecast(APIView):
    @method_decorator(ratelimit(key='ip', rate='30/m',method='POST'))
    def post(self, request, format=None):

        try:
            serializer = WeatherRequestSerializer(data=request.data)

            if serializer.is_valid():
                date_today = datetime.date.today()
                lat = serializer.validated_data['lat']
                lon = serializer.validated_data['lon']

                temperatures = Temperature.objects.filter(querydt=date_today, lat=lat, lon=lon).order_by('dt')[:5]
                data = TemperatureSerializer(temperatures, many=True).data

                if not data:
                    data = get_weather_data(lat=lat, lon=lon)

                    temperature_instances = [
                        Temperature(
                            dt=item['dt'],
                            day=item['day'],
                            min=item['min'],
                            max=item['max'],
                            night=item['night'],
                            eve=item['eve'],
                            morn=item['morn'],
                            lat=item['lat'],
                            lon=item['lon'],
                            querydt=date_today,
                        )
                        for item in data
                    ]

                    temperatures = Temperature.objects.bulk_create(temperature_instances)
                    data = TemperatureSerializer(temperatures, many=True).data

                return Response({"content": data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)