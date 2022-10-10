# from django import forms
import pandas as pd


location_df = pd.read_csv("기상청41_단기예보 조회서비스_오픈API활용가이드_격자_위경도(20220103).csv")
location_df = location_df[['1단계','2단계','3단계','격자 X','격자 Y']]
location_df.fillna('전체', inplace=True)

print(location_df['1단계'].unique())
