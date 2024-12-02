from django.db import models

# Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='部门名称', max_length=32)
    
    def __str__(self) -> str:
        return self.title
    
class User_info(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名', max_length=32)    
    pwd = models.CharField(verbose_name="密码",max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0) #数字长度为10，小数点后两位
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")
    
    gender_choices = ((0,'男'),(1,'女'))
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices,default=0)
    
    #级联删除
    depart = models.ForeignKey(verbose_name='部门',to="Department",to_field="id",
                               on_delete=models.CASCADE)
    #置空
    # depart = models.ForeignKey(to="Department",to_field="id",null=True,blank=True,
    #                            on_delete=models.SET_NULL)
    
    
class Admin_info(models.Model):
    """管理员"""
    username = models.CharField(verbose_name='用户名', max_length=32)
    pwd = models.CharField(verbose_name="密码",max_length=100)
    
    
    def __str__(self):
        return self.username
    
class Task(models.Model):
    level_choices = ((0,'紧急'),(1,'重要'),(2,'普通'))
    title = models.CharField(verbose_name='任务名称', max_length=32)
    level = models.SmallIntegerField(verbose_name='优先级',choices=level_choices,default=2)
    detail = models.TextField(verbose_name='任务详情')
    user = models.ForeignKey(verbose_name='负责人',to="Admin_info",to_field="id",on_delete=models.CASCADE)
    
    
class Order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=64)
    title = models.CharField(verbose_name='订单名称', max_length=32)
    price = models.IntegerField(verbose_name='订单金额')
    
    status_choices = (
        (1,'待支付'),
        (2,'已支付')
    )
    status = models.SmallIntegerField(verbose_name='订单状态',choices=status_choices,default=1)
    admin = models.ForeignKey(verbose_name='管理员',to="Admin_info",to_field="id",on_delete=models.CASCADE)
    
    
class City(models.Model):
    name = models.CharField(verbose_name='城市名称', max_length=32)
    count = models.IntegerField(verbose_name='人口数量')
    img = models.FileField(verbose_name='logo',upload_to='city')