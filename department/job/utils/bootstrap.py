from django import forms

class BoostrapForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        exclude = ['img']
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            if name in exclude:
                continue
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {"class":"form-control","placeholder":field.label}