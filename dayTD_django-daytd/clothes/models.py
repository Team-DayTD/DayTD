from django.db import models
from account.models import OurUser
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    si = models.CharField(max_length=40)
    gu = models.CharField(max_length=40)
    dong = models.CharField(max_length=40)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return '{} {} {} {} {}'.format(self.si, self.gu, self.dong, self.x, self.y)

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'region'

# 사용자가 지역 선택한 값 저장하기 위한 모델
class MyLocation(models.Model):
    # id = models.IntegerField()
    num_list = models.CharField(max_length=40)
    user_id = models.CharField(max_length=40)
    si = models.CharField(max_length=40)
    gu = models.CharField(max_length=40)
    dong = models.CharField(max_length=40)

    def __str__(self):
        return '{} {}'.format(self.gu, self.dong)

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'save_region'

# 옷    
class Clothes(models.Model):
    image = models.ImageField(upload_to='clothes', blank=True) # Pillow 라이브러리 필요
    id = models.IntegerField(primary_key=True)
    # 속성
    STYLE_CHOISE =(
        ("심플베이직", "simple&basic"),
        ("러블리", "lovely"),
        ("섹시글램", "sexy"),
        ("유니크", "unique"),
        ("유니섹스", "unisex"),
        ("빈티지", "vintage"),
        ("캐주얼", "casual"),
        ("기타", "etc")
    )
    style = models.CharField(choices=STYLE_CHOISE, max_length=40, default='')

    outerwear = models.JSONField(default='{}')
    top = models.JSONField(default='{}')
    pants = models.JSONField(default='{}')
    onepiece = models.JSONField(default='{}')

    max_tem = models.IntegerField()
    min_tem = models.IntegerField()

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'clothes'

class ClotheStyle(models.Model): # 회원가입 시 기본값이 들어가 있어야 작동함.
    num_list = models.CharField(max_length=40)
    user_id = models.CharField(max_length=40)
    user_style = models.CharField(max_length=40, default=all)
    
    # def __str__(self):
    #     return '{} {}'.format(self.user_id, self.user_style)

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'save_style'

class Likes(models.Model):
    # id = models.IntegerField()
    user = models.ForeignKey(OurUser, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    style = models.CharField(max_length=40)
    # 좋아요 여부
    like_select = models.BooleanField(default=False)

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'likes_test'



    


# class Si(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Gu(models.Model):
#     si = models.ForeignKey(Si, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

# class Dong(models.Model):
#     gu = models.ForeignKey(Gu, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

# class Region(models.Model):
#     si = models.ForeignKey(Si, on_delete=models.SET_NULL, blank=True, null=True)
#     gu = models.ForeignKey(Gu, on_delete=models.SET_NULL, blank=True, null=True)
#     dong = models.ForeignKey(Dong, on_delete=models.SET_NULL, blank=True, null=True)
#     x = models.IntegerField()
#     y = models.IntegerField()

#     def __str__(self):
#         return '{} {} {} {}'.format(self.gu, self.dong, self.x, self.y)
