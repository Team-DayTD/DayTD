# 공공데이터 : 기상청 단기예보 조회 서비스 - 초단기예보
from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
import os
import urllib 

from datetime import date, timedelta, datetime
# from DayTD.src import key.properties

# import mylib

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d

keyPath = os.path.join(os.getcwd(), 'our_weather','key.properties')
key = getKey(keyPath)
serviceKey = key['gokr']
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def check_weather(nx=60, ny=127):
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
    
    now = datetime.now()
    today = datetime.today().strftime("%Y%m%d")
    y = date.today() - timedelta(days = 1)
    yesterday = y.strftime("%Y%m%d")

    # nx = 60
    # ny = 127

    if now.minute < 45 :
        if now.hour == 0:
            base_time = "2330"
            base_date = yesterday
        else :
            pre_hour = now.hour-1
            if pre_hour < 10:
                base_time = '0' + str(pre_hour) + '30'
            else:
                base_time = str(pre_hour) + "30"
            base_date = today
    else:
        base_date = today

        if now.hour <10 :
            base_time = '0' + str(now.hour) + '30'
        else :
            base_time = str(now.hour) + '30'
        

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('numOfRows') : 60, 
                                    quote_plus('dataType') : 'xml', quote_plus('base_date') : base_date, 
                                    quote_plus('base_time') : base_time, quote_plus('nx') : nx, quote_plus('ny') : ny })

    # 웹 브라우저 서버에서 값 요청 - url주소와 파라미터
    res = requests.get(url+queryParams, verify=False)
    
    # 카테고리와 그에 상응하는 값을 각각 리스트로 저장
    category = [] 
    temperture =[]

    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')

    for tag in soup.find_all('category'):
        category.append(tag.text)
    for tag in soup.find_all('fcstvalue'):
        temperture.append(tag.text)

    # 두 리스트를 하나로 만듦
    data = []
    for i in range(0, len(category)):
        mylist = []
        mylist.append(category[i])
        mylist.append(temperture[i])
        data.append(mylist)

    weather_data = dict()

    for i in range(0, len(data)):
        dict1(weather_data, data[i][0], data[i][1])

    return weather_data

# 한 키에 여러 값을 가질 수 있도록 하기 위한 함수 
def dict1(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
        sample_dict[key].append(list_of_values)
    else:
        sample_dict[key].append(list_of_values)
    return sample_dict

def get_category(choice):
    res = check_weather()
    temp = res.get(choice)
    
    mydict = dict()
    for _tmp in range(0, len(temp)):
        mydict[_tmp] = temp[_tmp]

    return mydict

# gps
def get_gps():
    html_contents = 'http://127.0.0.1:8000/our_weather/gps/'
    my_loc = []
    elements = BeautifulSoup(html_contents, 'html.parser')

    for loc in elements.find_all('input'):
        my_loc.append(loc.tag)

    return my_loc