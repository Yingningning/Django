from django import forms
from job import models
from django.core.exceptions import ValidationError

from job.utils.bootstrap import BoostrapForm
from job.utils.encode import md5

class AdminModelFrom(BoostrapForm):
    
    confirm_pwd = forms.CharField(label='确认密码',widget=forms.PasswordInput)
    class Meta:
        model = models.Admin_info
        fields = ['username','pwd','confirm_pwd']
        widgets = {
            'pwd': forms.PasswordInput,
        }
    
    def clean_pwd(self):
        pwd = self.cleaned_data.get('pwd')
        return md5(pwd)
    
    
    # """在 Django 的表单（Form）类中，clean_ 前缀的方法具有特殊意义，它们会自动执行。当你调用 form.is_valid() 或 form.clean() 时，Django 会自动调用这些 clean_ 前缀的方法来进行数据验证。"""
    def clean_confirm_pwd(self): #
        pwd = self.cleaned_data.get('pwd')
        confirm = md5(self.cleaned_data.get('confirm_pwd'))
        print(pwd,confirm)
        if pwd != confirm:
            raise ValidationError('两次密码输入不一致')
        return confirm
    
class AdminEditModelFrom(BoostrapForm):
    class Meta:
        model = models.Admin_info
        fields = ['username']
        
class Account(BoostrapForm):
    code = forms.CharField(label='验证码')
    class Meta:
        model = models.Admin_info
        fields = ['username','pwd','code']
        widgets = {
            'pwd': forms.PasswordInput
        }
        
    def clean_pwd(self):
        pwd = self.cleaned_data.get('pwd')
        return md5(pwd)
        

class TaskForm(BoostrapForm):
    class Meta:
        model = models.Task
        fields = '__all__'

class OrderForm(BoostrapForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ['oid','admin']
        
class UpModelForm(BoostrapForm):
    
    class Meta:
        model = models.City
        fields = '__all__'
        