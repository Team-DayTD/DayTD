from django.shortcuts import render
from .short_weather_api import *
from .map_grid import mapToGrid, gridToMap
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse  
from django.views.generic import View
# 장고 위변조 방지
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# 메인화면
# @csrf_exempt # 위변조 방지
class WeatherListAPI(APIView):
    def get(self, request):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

        nx, ny = mapToGrid(float(lat), float(lon))

        res = check_weather(nx, ny)

        # 현재 기온 ('C)
        _temperture = res.get("T1H")
        temperture = _temperture[0]

        # 현재 강수량 (mm)
        _rain = res.get("RN1")
        rain = _rain[0]

        # 습도 (%)
        _humid = res.get("REH")
        humid = _humid[0]

        # 하늘 상태 : 맑음(1), 구름많음(3), 흐림(4)
        _sky = res.get("SKY")
        sky = _sky[0]

    
        context = {'temperture': temperture, 'rain':rain, 'humid':humid, 'sky':sky, 'nx':nx, 'ny':ny}
        print(context)
        return Response(context)

# 온도 그래프 확인 화면
def detail(request):
    # 위도 경도
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    nx, ny = mapToGrid(float(lat), float(lon))

    res = check_weather(nx, ny)

    # 현재 기온 ('C)
    _temperture = res.get("T1H")
    temperture = _temperture[0]

    # 현재 강수량 (mm)
    _rain = res.get("RN1")
    rain = _rain[0]

    # 습도 (%)
    _humid = res.get("REH")
    humid = _humid[0]

    # 하늘 상태 : 맑음(1), 구름많음(3), 흐림(4)
    _sky = res.get("SKY")
    sky = _sky[0]

 
    context = {'temperture': temperture, 'rain':rain, 'humid':humid, 'sky':sky, 'nx':nx, 'ny':ny}
    print(context)
    return render(request, 'our_weather/our_detail.html', context)

# gps 테스트
def gps(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    # submit_chk=request.GET.get('submit_chk')

    # lat, lon = get_gps()
    context = {'lat':lat, 'lon':lon}
    print(context)
    return render(request, 'our_weather/gps.html', context)
