from os import stat
from django import forms
from django.forms import widgets
from django.forms import fields
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput, Select
from .models import models, options_std
# class create_repair(forms.Form):
#     id_lb =forms.CharField(max_length=255)
#     subject = forms.CheckboxInput()

class opsForm(forms.Form):
    text =[
        ('201',201),
        ('202',202),
        ('203',203),
        ('204',204),
        ('205',205),
        ('206',206),
        ('207',207),
        ('208',208),
    ]
    field = forms.ChoiceField(
        required=False,
        label='',
        label_suffix='   ',
        choices=text,
        widget=forms.Select(attrs={'class':'form-control','style':'text-align:center;width:60px;height:28px;padding:0px 7px;font-size:15px;margin-top:-5px'}),
    )
    # field.widget.attrs.update({'class':'form-control','style':'text-align:center;width:60px;height:28px;padding:0px 7px;font-size:15px;margin-top:-5px'})
    
class adminsForm(forms.Form):
    text = [
        ('201',201),
        ('202',202),
        ('203',203),
        ('204',204),
        ('205',205),
        ('206',206),
        ('207',207),
        ('208',208),
        ('103',103),
        ('104',104),
        ('105',105),
        ('106',106),
        ('ทะเบียน',"ทะเบียน"),
        ('ประชาสัมพันธ์',"ประชาสัมพันธ์"),
        ('CareerHub',"CareerHub"),
        ('การเงิน',"การเงิน"),
    ]
    field = forms.ChoiceField(
        required=False,
        label='',
        label_suffix='   ',
        choices=text,
        widget=forms.Select(attrs={'class':'form-control','style':'text-align:center;width:110px;height:28px;padding:0px 7px;font-size:15px;margin-top:-5px'}),
    )

class repiarForm(forms.Form):
    text = [
        ('103',103),
        ('104',104),
        ('105',105),
        ('106',106),
        ('ทะเบียน',"ทะเบียน"),
        ('ประชาสัมพันธ์',"ประชาสัมพันธ์"),
        ('CareerHub',"CareerHub"),
        ('การเงิน',"การเงิน"),
    ]
    field = forms.ChoiceField(
        required=False,
        label='',
        label_suffix='   ',
        choices=text,
        widget=forms.Select(attrs={'class':'form-control','style':'text-align:center;width:110px;height:28px;padding:0px 7px;font-size:15px;margin-top:-5px'}),
    )

class input_detail(forms.Form):
    textinput = forms.CharField()


    # https://docs.djangoproject.com/en/3.1/topics/forms/
    # https://pypi.org/project/django-bootstrap-modal-forms/2.0.0/
    # https://stackoverflow.com/questions/37170465/how-to-get-value-checkbox-on-modal-bootstrap
    # boolean Field   https://www.youtube.com/watch?v=C4P5fiAC7QA&ab_channel=DJanGO
    # git hub https://github.com/showkuay97/ctrlsystem.git
    #https://stackoverflow.com/questions/45310054/passing-data-form-datatable-to-modal-django/45317822