from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# class OurUser(models.Model):
#     id = models.CharField(max_length=40)
#     password = models.CharField(max_length=40)
#
#     GENDER_CHOISE =(
#         ("W", "woman"),
#         ("M", "man"),
#         ("No", "none")
#     )
#     gender = models.CharField(choices=GENDER_CHOISE ,max_length=2)
#     birth = models.DateField()
#     email = models.EmailField(max_length=254)
#
#     def __str__(self):
#         return self.id
#
#     class Meta:
#         managed = False
#         app_label = "mysqldb"
#         db_table = 'users'

class OurUser(models.Model):
    # id = models.IntegerField()
    user = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=40)

    GENDER_CHOISE =(
        ("W", "woman"),
        ("M", "man"),
        ("No", "none")
    )
    gender = models.CharField(choices=GENDER_CHOISE ,max_length=2)
    birth = models.DateField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user

    class Meta:
        managed = False
        app_label = "mysqldb"
        db_table = 'users'

