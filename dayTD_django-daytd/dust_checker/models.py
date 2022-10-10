from django.db import models

# Create your models here.
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    lon = models.FloatField(blank=True, null=True) #경도
    lat = models.FloatField(blank=True, null=True) #위도
    description = models.CharField(max_length=100, blank=True, null=True)
  
    def __str__(self):
        return str(self.building_name)


class WeatherDB(models.Model):
    building = models.ForeignKey('Building', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    temp = models.IntegerField(blank=True, null=True) #온도
    humidity = models.IntegerField(blank=True, null=True) #습도
    rainType = models.CharField(max_length=20, blank=True, null=True) #한시간 동안 강수량
    sky = models.IntegerField(blank=True, null=True) # 하늘 상태

    def __str__(self):
        return str(self.building) + " - " + str(self.timestamp)