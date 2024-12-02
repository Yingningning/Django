from django.shortcuts import render,redirect
from num import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from num.utils.bootstrap import BoostrapForm
# from django.core.paginator import mar


class NumberForm(forms.models.ModelForm):
    
    """验证方式1"""
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    # )
    
    class Meta:
        model = models.Number
        # nums = "__all__" #取所有字段
        fields = ["mobile","price","level","status"]
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {"class":"form-control","placeholder":field.label}

    
    """验证方式2"""
    def clean_mobile(self):
        text = self.cleaned_data['mobile']
        exists = models.Number.objects.filter(mobile=text).exists()
        if exists:
            raise ValidationError('手机号已存在')
        if len(text) != 11:
            raise ValidationError('手机号长度不正确')
        return text
    
from num.utils.Pagenation import Pagenation
# Create your views here.
def num_list(request):
    # for i in range(200):
    #     models.Number.objects.create(mobile='1380013800%s'%i,price=100,level=1,status=1)
    data_dict = {}
    q = request.GET.get('q')
    if q:
        data_dict['mobile__contains'] = q
        
    page_size = 9    
    page_param = 'page'
    plus = 5
    
    nums = models.Number.objects.filter(**data_dict).all()
    page_objection = Pagenation(request,nums,page_size,plus,page_param)
    page_querset = page_objection.page_queryset
    
    page_str = page_objection.html()
  
    
    return render(request,'num_list.html',{'nums':page_querset,'page_str':page_str})

def num_add(request):
    if request.method == "GET":
        form = NumberForm()
        return render(request,'num_add.html',{'form':form})
    form = NumberForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/num_list')
    return render(request,'num_add.html',{'form':form})


class NumberEditForm(BoostrapForm):
    mobile = forms.CharField(disabled=True,label="手机号")
    class Meta:
        model = models.Number
        # nums = "__all__" #取所有字段
        fields = ["mobile","price","level","status"]
        
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for name,field in self.fields.items():
    #         field.widget.attrs = {"class":"form-control","placeholder":field.label}

def num_edit(request,nid):
    num = models.Number.objects.filter(id = nid).first()
    if request.method == "GET":
        form = NumberEditForm(instance=num)
        return render(request,'num_edit.html',{'form':form})
    form = NumberEditForm(request.POST,instance=num)
    if form.is_valid():
        form.save()
        return redirect('/num_list')
    return render(request,'num_edit.html',{'form':form})

def num_del(rquest,nid):
    models.Number.objects.filter(id = nid).delete()
    return redirect('/num_list')