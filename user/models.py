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

