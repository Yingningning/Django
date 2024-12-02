from django.db import models

# Create your models here.
class Number(models.Model):
    
    mobile = models.CharField(verbose_name='手机号',max_length=32)
    price = models.IntegerField(verbose_name='价格')
    
    level_choices = (
        (1,'普通用户'),
        (2,'VIP')
    )
    level = models.SmallIntegerField(verbose_name='用户等级',choices=level_choices,default=1)
    
    status_choices = (
        (1,'未售'),
        (2,'已售')
        )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)
    