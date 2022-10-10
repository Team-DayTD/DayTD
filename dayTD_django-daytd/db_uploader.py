import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","DayTD.settings")
django.setup()

from clothes.models import *

CSV_PATH = "C:/Users/Songhee/Desktop/2022-1/졸업프로젝트/날씨데이터/location.csv"


# with open(CSV_PATH, newline='', encoding='cp949') as csv_file:
#     data_reader = csv.DictReader(csv_file)
#     for row in data_reader:
#         print(row)
#         Location.objects.create(
#             si = row['1단계'],
#             gu = row['2단계'],
#             dong = row['3단계'],
#             x = row['격자 X'],
#             y = row['격자 Y'],
#         )


def insert_si():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Si.objects.filter(name=row['si']).exists():
                si_id = Si.objects.create(name=row['si'])
    print('SI DATA UPLOADED SUCCESSFULY!')


def insert_gu():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Gu.objects.filter(name=row['gu']).exists():
                si_id = Si.objects.get(name=row['si'])
                Gu.objects.create(
                    name=row['gu'],
                    si=si_id,
                )
    print('GU DATA UPLOADED SUCCESSFULY!')

def insert_dong():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Dong.objects.filter(name=row['dong']).exists():
                gu_id = Gu.objects.get(name=row['gu'])
                Dong.objects.create(
                    name=row['dong'],
                    gu=gu_id,
                )
    print('DONG DATA UPLOADED SUCCESSFULY!')

def insert_region():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            si_id = Si.objects.get(name=row['si'])
            gu_id = Gu.objects.get(name=row['gu'])
            dong_id = Dong.objects.get(name=row['dong'])

            Region.objects.create(x=row['x'],
                                   y=row['y'],
                                   si=si_id,
                                   gu=gu_id,
                                   dong=dong_id,)
    print('PRODUCT DATA UPLOADED SUCCESSFULY!')

# insert_si()
# insert_gu()
# insert_dong()
# insert_region()

# ------------------------------------------------------------------------
def insert_country():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Country.objects.filter(name=row['si']).exists():
                si_id = Country.objects.create(name=row['si'])
    print('SI DATA UPLOADED SUCCESSFULY!')


def insert_city():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not City.objects.filter(name=row['gu']).exists():
                si_id = Country.objects.get(name=row['si'])
                City.objects.create(
                    name=row['gu'],
                    country=si_id,
                )
    print('GU DATA UPLOADED SUCCESSFULY!')

def insert_dong():
    with open(CSV_PATH, newline='', encoding='cp949') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            if not Person.objects.filter(name=row['dong']).exists():
                gu_id = City.objects.get(name=row['gu'])
                si_id = Country.objects.get(name=row['si'])
                Person.objects.create(
                    name=row['dong'],
                    country=si_id,
                    city=gu_id,
                )
    print('DONG DATA UPLOADED SUCCESSFULY!')
#
# insert_country()
# insert_city()

insert_dong()