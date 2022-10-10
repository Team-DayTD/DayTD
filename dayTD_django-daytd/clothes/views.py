import random
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import *
from .models import *
from .serializers import *

from .map_grid import gridToMap, mapToGrid
from our_weather.short_weather_api import check_weather
from .mobilenet import *
from django.db.models import Count
from django.db.models import Q
import base64
from PIL import Image
from io import BytesIO
import pickle
from convert_to_queryset import list_to_queryset

# 메인 화면 코디 출력
class MainClothesListAPI(APIView):
    '''
        1. 좋아요 필터링 - AI 추천 오늘의 코디
            today_clothes
        2. 좋아요 *스타일 필터링 - AI 추천 캐주얼룩
            my_clothes
        3. 랜덤코디(X) - 좋아요 탑 8
            ran_clothes 
    '''

    def get(self, request):
        # 2. 좋아요 스타일 필터링 - AI 추천 캐주얼룩
        user_clothes = Likes.objects.values('style').annotate(Count('style'))
        style = user_clothes[0]['style'] # 좋아요가 가장 많았던 스타일
        clothes = Clothes.objects.filter(style = style)

        # ** 날씨 필터링
        nx = request.GET.get('nx')
        ny = request.GET.get('ny')
        if nx is not None:
            res = check_weather(nx, ny)
        else:
            res = check_weather()

        _temperture = res.get("T1H")  # 현재 기온 ('C)
        temperture = _temperture[0]
        

        # 2번 : 스타일 필터링 이후에 날씨 필터 - for 범위가 다름
        count = clothes.values('id').aggregate(count=Count('id'))
        clothes_value = clothes.values()

        result = []  # queryset 저장 리스트
        for j in range(count['count']):
            if clothes_value[j]['max_tem'] == 50:
                _min_tem=[]
                _min_tem.append(int(temperture))

                for i in range(5):
                    _min_tem.append(int(temperture)-i)

                my_clothes = Clothes.objects.filter(style__in=[style], min_tem__in=_min_tem)

            elif clothes_value[j]['min_tem'] == -50:
                _max_tem=[]
                _max_tem.append(int(temperture))

                for i in range(5):
                    _max_tem.append(int(temperture)+i)

                my_clothes = Clothes.objects.filter(style__in=[style], max_tem__in=_max_tem)

            else:
                else_max_tem = (int(temperture) + 5)
                else_min_tem = (int(temperture) - 5)

                clothes_list = []

                for _clothes in clothes_value:
                    avg = (_clothes['max_tem'] + _clothes['min_tem'])/2

                    if ((avg < else_max_tem) and (avg > else_min_tem)):
                        clothes_list.append(_clothes['id'])
            
                my_clothes = Clothes.objects.filter(style__in=[style], id__in=clothes_list) #필터링 완료된 쿼리셋

            result.append(my_clothes)

        _my = result[0] | result[1]
        for i in range(2, count['count']):
            _my = _my | result[i]

        # 1, 3 => 총 16개 전달
        clothes2 = Clothes.objects.all()
        count2 = clothes2.values('id').aggregate(count=Count('id'))
        clothes_value2 = clothes2.values()

        result2 = []  # queryset 저장 리스트
        for j in range(count2['count']):
            if clothes_value2[j]['max_tem'] == 50:
                _min_tem=[]
                _min_tem.append(int(temperture))

                for i in range(5):
                    _min_tem.append(int(temperture)-i)

                today_clothes = Clothes.objects.filter(min_tem__in=_min_tem)

            elif clothes_value2[j]['min_tem'] == -50 :
                _max_tem=[]
                _max_tem.append(int(temperture))

                for i in range(5):
                    _max_tem.append(int(temperture)+i)

                today_clothes = Clothes.objects.filter(max_tem__in=_max_tem)
                
            else:
                else_max_tem = (int(temperture) + 5)
                else_min_tem = (int(temperture) - 5)

                clothes_list = []

                for _clothes in clothes_value2:
                    avg = (_clothes['max_tem'] + _clothes['min_tem'])/2
                    if ((avg < else_max_tem) and (avg > else_min_tem)):
                        clothes_list.append(_clothes['id'])

                today_clothes = Clothes.objects.filter(id__in=clothes_list)
            result2.append(today_clothes)

        _today = result2[0] | result2[1]
        for i in range(2, count2['count']):
            _today = _today | result2[i]

        # 3.랜덤
        _ran_clothes = Clothes.objects.all()
        ran_clothes_list = list(_ran_clothes)
        random.shuffle(ran_clothes_list)
        ran_clothes = ran_clothes_list[:8]

        today = _today[:8]#.values_list('id', flat=True) #1
        my = _my[:16]#.values_list('id', flat=True) #2

        today_serializer = ClothesSerializer(data=today, many=True)
        my_serializer = ClothesSerializer(data=my, many=True)
        ran_serializer = ClothesSerializer(data=ran_clothes, many=True)

        if (today_serializer.is_valid() & my_serializer.is_valid() & ran_serializer.is_valid()):
            today_serializer.save()
            my_serializer.save()
            ran_serializer.save()

        context = {
            'today': today_serializer.data,
            'my': my_serializer.data,
            'ran': ran_serializer.data
        }

        return Response(context, status=status.HTTP_201_CREATED)

# # 코디 추천 -스타일 선택
# # # html-js로 테스트 입력
# @method_decorator(csrf_exempt, name='dispatch')
# def style_test(request):
#     style = request.GET.get('style')
#     context = {'style':style}
#     return render(request, 'clothes/style.html', context)


# 스타일 선택
class StyleListAPI(APIView):
    def get(self, request):
        style = request.GET.get('style')

        clothes = Clothes.objects.filter(style__in=[style])
        print(clothes)
        serializer = ClothesSerializer(data=clothes, many=True)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

# 사용자 입력 스타일
class MyStylePostAPI(APIView):
    def post(self,request):
        serializer = MyStyleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyStyleAPI(APIView):
    def get(self,request):
        user_id = request.GET.get('user_id')
        num_list = request.GET.get('num_list')

        print('-------user_id---------',user_id)
        my_style = ClotheStyle.objects.filter(user_id__in=[user_id], num_list__in=[num_list]).order_by().last()

        if my_style == None:
            content = {'user_id': user_id, 'user_style': '캐주얼'}
            return Response(content)

        content = {'user_id': my_style.user_id, 'user_style': my_style.user_style}
        print(my_style)

        return Response(content)
       

# 코디 - 지역 선택 : 전체 지역
class LocationListAPI(APIView):
    def get(self, request):
        location = Location.objects.all()
        serializer = LocationModelSerializer(location, many=True)
        print(serializer)
        return Response(serializer.data)

# 코디 - 지역 선택 : 사용자 입력 저장
class MyLocationPostListAPI(APIView):
    def post(self, request):
        serializer = MyLocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyLocationGetListAPI(APIView):
    def get(self, request):
        user = request.GET.get('user_id')
        num_list = request.GET.get('num_list')
        my_location = MyLocation.objects.filter(user_id__in=[user], num_list__in=[num_list]).order_by().last()
        print('--------user-------\n',user)
        print('--------num_list-------\n', num_list)
        print('--------my_location-------\n', my_location)
        if my_location == None:
            location = Location.objects.first()
        else:
            location = Location.objects.filter(si__in=[str(my_location.si)], gu__in=[str(my_location.gu)],dong__in=[str(my_location.dong)]).order_by().last() # si__in=[str(my_location.si)], gu__in=[str(my_location.gu)],

        print('---------------------', location)
        location_json = {'id': location.id, 'si':location.si, 'gu':location.gu, 'dong':location.dong, 'nx':location.x, 'ny':location.y}
        print(location_json)

        return Response(location_json)

features={} #스타일별 옷들 feature
clothes_tuple={} #스타일별 옷 리스트
class CodiArrayAPI(APIView): #코디 추천 모델_모든 파일 feature 추출
    def get(self, request):
        fe = FeatureExtractor()

        features_list = []

        list1=[] #db에서 불러와서 리스트 생성, 카테고리 필터링한 옷 이름들
        # style_list=['casual', 'unique', 'simplebasic', 'lovely', 'sexyglam', 'vintage', 'unisex', 'etc']
        style_list = ['캐주얼','유니크', '심플베이직', '러블리', '섹시글램', '빈티지', '유니섹스', '기타']

        for i in style_list:
            style_clothes=Clothes.objects.filter(style__in=[i]).values('id') #<QuerySet [{'id': 100035}, {'id': 100049}, {'id': 100161},...
            # print(style_clothes)
            count = style_clothes.aggregate(count=Count('id')) #총 개수 세기

            for j in range(count['count']):
                val=str(Clothes.objects.filter(style__in=[i]).values('id')[j]['id']) #100035 같은 스타일 옷들 추출
                list1.append(val)

                clothes_list1 = Clothes.objects.get(id=val)#Clothes object (100035)
                #Clothes.objects.get(id=l[:-4])
                image_data = base64.b64encode(clothes_list1.image).decode('utf-8')
                base64_decoded = base64.b64decode(image_data)
                feature = fe.extract(Image.open(BytesIO(base64_decoded)))
                features_list.append(feature)

                # Save the Numpy array (.npy) on designated path 현재 저장 안해도 돌아감
                # feature_path = "./clothes/model/feature/" + style + "/" + val[:-4] + ".npy"
                # np.save(feature_path, features_list)
            global features
            global clothes_tuple
            features[i]=features_list
            clothes_tuple[i]=list1

        # save data
        with open('clothes/pickles/features.pickle', 'wb') as fw:
            pickle.dump(features, fw)

        with open('clothes/pickles/clothes_tuple.pickle', 'wb') as fw:
            pickle.dump(clothes_tuple, fw)
      

# 찜과 비슷한 옷 추출 -> 추출한 옷에서 현재 기온 반영 온도 필터링
class LocationWeatherListAPI(APIView):
    def get(self, request):
        user = request.GET.get('user')
        # style = request.GET.get('style')
        _style = ClotheStyle.objects.filter(user_id__in=[user]).last()

        if _style == None:
            style = '캐주얼'
        else:
            style = _style.user_style


        with open('clothes/pickles/features.pickle', 'rb') as fr:
            features = pickle.load(fr)

        with open('clothes/pickles/clothes_tuple.pickle', 'rb') as fr:
            clothes_tuple = pickle.load(fr)

        print("-----------user------------\n", user)
        print("-----------style------------\n",style)
        like_object = Likes.objects.filter(style__in=[style]).last() #제일 최근 찜, Likes object (8)
        # like_object = Likes.objects.values()
        print(like_object)
        if like_object != None:
            like_clothes_id=like_object.clothes_id #찜한 옷, Clothes object (100161)

            like_clothes_id = Clothes.objects.get(id=like_clothes_id)
            print('----------like_clothes_id-------------', like_clothes_id)
            image_data2 = base64.b64encode(like_clothes_id.image).decode('utf-8')
            base64_decoded2 = base64.b64decode(image_data2)
            fe2 = FeatureExtractor()
            #feature2 = fe2.extract(Image.open(BytesIO(base64_decoded2)))
            # Extract its features
            query = fe2.extract(Image.open(BytesIO(base64_decoded2)))

            # Calculate the similarity (distance) between images
            dists = np.linalg.norm(features[style] - query, axis=1)

            # Extract 30 images that have lowest distance
            ids = np.argsort(dists)[1:31] #옷 30개 추출

            scores = [(dists[id], clothes_tuple[style][id], id) for id in ids]

            # Visualize the result
            results=[]
            for a in range(30):
                score = scores[a]
                results.append(score[1]) #추출한 옷번호
            print('------results-----',results)
            nx = request.GET.get('nx')
            ny = request.GET.get('ny')

            if nx is not None:
                res = check_weather(nx, ny)
            else:
                res = check_weather()

            # 현재 기온 ('C)
            _temperture = res.get("T1H")
            temperture = _temperture[0]
            print('-------tem: ', temperture)

            # 현재 강수량 (mm)
            _rain = res.get("RN1")
            rain = _rain[0]
            print('----------ok3-------------')

            clothes_ = Clothes.objects.filter(style__in=[style])
            print('----------filter clothes------------')
            clothes_count = clothes_.values('id')
            count = clothes_count.aggregate(count=Count('id'))  # 총 개수 세기

            clothes = clothes_.values()

            result = [] # queryset 저장 리스트
            for j in range(count['count']):
                # print('---------j--------',j)
                if clothes[j]['max_tem'] == 50:
                    _min_tem=[]
                    _min_tem.append(int(temperture))

                    for i in range(5):
                        _min_tem.append(int(temperture)-i)
                    my_clothes = Clothes.objects.filter(style__in=[style], min_tem__in=_min_tem)

                elif clothes[j]['min_tem'] == -50 :
                    _max_tem=[]
                    _max_tem.append(int(temperture))

                    for i in range(5):
                        _max_tem.append(int(temperture)+i)
                    my_clothes = Clothes.objects.filter(style__in=[style], max_tem__in=_max_tem)

                else:
                    else_max_tem = (int(temperture) + 5)
                    else_min_tem = (int(temperture) - 5)

                    clothes_list = []

                    for _clothes in clothes:
                        avg = (_clothes['max_tem'] + _clothes['min_tem'])/2
                        if ((avg < else_max_tem) and (avg > else_min_tem)):
                            clothes_list.append(_clothes['id'])

                    my_clothes = Clothes.objects.filter(id__in=clothes_list) #필터링 완료된 쿼리셋
                    # print('-----------!!-------------',my_clothes.id)
                result.append(my_clothes)

            my_clothes = result[0] | result[1]
            for i in range(2,count['count']):
                my_clothes = my_clothes | result[i]

            print('-------------my_clothes------',my_clothes)

            count2 = my_clothes.aggregate(count=Count('id'))  # 총 개수 세기
            for a in range(len(results)): # results : 찜이랑 비슷한 옷 추출 결과 (30개)
                for z in range(count2['count']):
                    id_num=my_clothes.values('id')[z]['id']
                    #print('---------id_num & results-----', id_num, results[a])
                    if results[a] == id_num: # !!!같은거 나오는지 확인 필요!!!
                        print('---------id_num-----',id_num)
                        codi=Clothes.objects.get(id=results[a])
                        serializer = ClothesSerializer(codi)

                        return Response(serializer.data)
                        break
            #날씨 추출 옷!=찜 비슷 옷
            codi=my_clothes[random.randrange(0, count2['count'])]
            print('-------------codi--------',codi)
            serializer = ClothesSerializer(codi)
            return Response(serializer.data)
        else: #찜이 없을때
            nx = request.GET.get('nx')
            ny = request.GET.get('ny')

            if nx is not None:
                res = check_weather(nx, ny)
            else:
                res = check_weather()

            # 현재 기온 ('C)
            _temperture = res.get("T1H")
            temperture = _temperture[0]

            # 현재 강수량 (mm)
            _rain = res.get("RN1")
            rain = _rain[0]

            clothes_ = Clothes.objects.filter(style__in=[style])
            clothes_count = clothes_.values('id')
            count = clothes_count.aggregate(count=Count('id'))  # 총 개수 세기

            clothes = clothes_.values()

            weather_result = []
            for j in range(count['count']):
                if clothes[j]['max_tem'] == 50:
                    _min_tem=[]
                    _min_tem.append(int(temperture))

                    for i in range(5):
                        _min_tem.append(int(temperture)-i)
                    my_clothes = Clothes.objects.filter(style__in=[style], min_tem__in=_min_tem)

                elif clothes[j]['min_tem'] == -50 :
                    _max_tem=[]
                    _max_tem.append(int(temperture))

                    for i in range(5):
                        _max_tem.append(int(temperture)+i)
                    my_clothes = Clothes.objects.filter(style__in=[style], max_tem__in=_max_tem)

                else:
                    else_max_tem = (int(temperture) + 5)
                    else_min_tem = (int(temperture) - 5)

                    clothes_list = []

                    for _clothes in clothes:
                        avg = (_clothes['max_tem'] + _clothes['min_tem']) / 2
                        if ((avg < else_max_tem) and (avg > else_min_tem)):
                            clothes_list.append(_clothes['id'])

                    my_clothes = Clothes.objects.filter(id__in=clothes_list)  # 필터링 완료된 쿼리셋
                    # print('-----------!!-------------',my_clothes.id)
                weather_result.append(my_clothes)
            print('------------no-------------')
            my_clothes = weather_result[0] | weather_result[1]
            for i in range(2, count['count']):
                my_clothes = my_clothes | weather_result[i]
            count2 = my_clothes.aggregate(count=Count('id'))

            codi = my_clothes[random.randrange(0, count2['count'])]
            serializer = ClothesSerializer(codi)
 
            return Response(serializer.data)

# 찜기능
class LikeListAPI(APIView):
    def get(self, request):
        
        like_clothes = Likes.objects.all()
        like_serializer = LikeSerializer(data=like_clothes, many=True)

        if like_serializer.is_valid():
            like_serializer.save()
        return Response(like_serializer.data)

class LikePostAPI(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikePutAPI(APIView):
    def put(self, request):
        like_data = request.data
        print('------',like_data)
        user = like_data['user']
        clothes = like_data['clothes']
        style = like_data['style']

        data = Likes.objects.filter(user__in=[user], clothes__in=[clothes], style__in=[style]).first()
        serializer = LikeSerializer(instance=data, data=like_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 시구동 선택
def sigudong_select_view(request):
    form = SigudongForm()
    if request.method == 'POST':
        form = SigudongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('load_xy')

    return render(request, 'location/home.html', {'form': form})

