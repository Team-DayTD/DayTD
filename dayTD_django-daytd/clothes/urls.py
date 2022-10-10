from django.urls import path
from clothes import views
from django.contrib.auth import views as auth_view

from .views import *

urlpatterns = [
    # 메인화면 코디 출력
    path('api/main/', MainClothesListAPI.as_view()),

    # 스타일 선택
    path('style/', views.style_test),
    path('style/api/', StyleListAPI.as_view()),

    # 전체 지역 출력
    path('api/location/', LocationListAPI.as_view()),
    
    # 사용자 입력 지역 선택
    path('api/my_location/post/',MyLocationPostListAPI.as_view()),
    path('api/my_location/', MyLocationGetListAPI.as_view()),

    # 모든 옷 데이터 feature
    path('api/location/codidata/', CodiArrayAPI.as_view()),

    # 시구동을 넣으면(프론트) 날씨 출력, 날씨에 맞는 찜과 유사한 옷 출력
    path('api/clothes/', LocationWeatherListAPI.as_view()),
    
    # 사용자 입력 코디 스타일 선택
    path('api/my_style/post/', MyStylePostAPI.as_view()),
    path('api/my_style/', MyStyleAPI.as_view()),

    # path('api/clothes/', LocationWeatherListAPI.as_view()),

    # 찜 목록 호출
    path('api/likes/', LikeListAPI.as_view()),

    # 찜 post
    path('api/likes/post/', LikePostAPI.as_view()),

    path('api/likes/put/', LikePutAPI.as_view()),
]
