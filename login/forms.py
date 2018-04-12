from django import forms
from django.forms import widgets
from django.forms import fields
from login.models import user,report,hospital
from django.core.validators import RegexValidator
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class UserForm(forms.Form):
    username = forms.CharField(label="DOCTOR", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #levels = forms.CharField(label="LEVEL", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    


class ReportForm(forms.Form):
    rep_status = (
        ('SAVED', 'SAVED'),
        ('PRINTED', 'PRINTED'),
        ('SENT', 'SENT'),
    )
    types =(
        ('X-RAY', 'X-RAY'),
        ('CT', 'CT'),
        ('MRI', 'MRI'),
    )
    gender = (
        ('M', "M"),
        ('F', "F"),
        ('Other', "Other")
    )
    unit = (
        ('D', "D"),
        ('W', "W"),
        ('M', "M"),
        ('Y', "Y"),
        (' ', " "),
    )
    examnum = forms.CharField(label="EXAM ID", max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="PATIENT NAME", max_length=40,widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(label="SEX", widget=forms.widgets.Select(choices=gender,attrs={'class': "form-control"}))
    age = forms.CharField(label="AGE", max_length=32,widget=forms.TextInput(attrs={'class': 'form-control'}))
    ageunit = forms.CharField(widget=forms.widgets.Select(choices=unit,attrs={'class': "form-control"}))
    position = forms.CharField(label="POSITION",max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    examtype = forms.CharField(label="EXAM TYPE",widget=forms.widgets.Select(choices=types,attrs={'class': "form-control"}))
    method = forms.CharField(label="EXAM METHOD",max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hospital = forms.CharField(label="HOSPITAL",widget=widgets.Select(choices=[],attrs={'class': "form-control"}),required=False)
    indication = forms.CharField(label="INDICATION",max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False) # 加入required 使得页面中表单内容为必填或不必填
    findings = forms.CharField(label="FINDINGS", widget=forms.Textarea(attrs={'class': 'form-control'}))
    comments = forms.CharField(label="COMMENTS", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    examdate = forms.DateField(label="EXAM DATE", widget=DateWidget(bootstrap_version=3, usel10n=True,attrs={'class': "form-control"}))
    reportdate = forms.DateField(label="REPORT DATE", widget=DateWidget(bootstrap_version=3, usel10n=True,attrs={'class': "form-control"}))
    repdoctor = forms.CharField(label="REPORT DOCTOR",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.CharField(widget=forms.widgets.Select(choices=rep_status,attrs={'class': "form-control"}))

    def __init__(self,*args, **kwargs):
        super(ReportForm,self).__init__(*args, **kwargs)
        self.fields['hospital'].widget.choices = hospital.objects.all().values_list('id','hosname')
    #缺少的列名
    
    #c_time = forms.DateTimeField(auto_now_add=True)    




        


