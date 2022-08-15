import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    SEX = (
        ('M', 'nan'),
        ('F', 'nv')
    )
    nickname = models.CharField(max_length=16, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)

    birth_year = models.IntegeField()
    birth_month = models.IntegeField()
    birth_day = models.IntegeField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (now - birth_date).days // 365

class Profile(models.Model):
    SEX = (
        ('M', 'nan'),
        ('F', 'nv')
    )

    location = models.CharField(max_length = 32, verbose_name='目标城市')

    min_distance = models.IntegeField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegeField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegeField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegeField(default=18, verbose_name='最大交友年龄')

    dating_sex = models.CharField(verbose_name='匹配的性别')
    vibration = models.Field(verbose_name='开启震动')
    only_matche = models.Field(verbose_name='不让为匹配的人看我的相册')
    auto_play = models.Field(verbose_name='自动播放视频')

