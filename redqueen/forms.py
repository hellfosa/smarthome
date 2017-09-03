from django import forms
from django.conf import settings


class MessageForm(forms.Form):
    Channel = forms.CharField(label='Channel', max_length=200)
    Signal = forms.CharField(label='Signal', max_length=200)

class RuleForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Group = forms.CharField(max_length=200)
    Action = forms.CharField(max_length=200)
    Start_at = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    End_at = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS)
    Repeat = forms.CharField(max_length=200)

class DeviceForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Group = forms.CharField(max_length=200)
    Value = forms.CharField(max_length=200)
    Channel = forms.CharField(max_length=200)

class HumanForm(forms.Form):
    Name = forms.CharField(max_length=200)
    Sex = forms.CharField(max_length=200)
    Role = forms.CharField(max_length=200)
    Phone = forms.CharField(max_length=200)
    Photo = forms.FileField()