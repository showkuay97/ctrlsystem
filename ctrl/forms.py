from os import stat
from django import forms
from django.forms import widgets
from django.forms.widgets import Select
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
        label='ห้องปฏิบัติการ',
        label_suffix='   ',
        choices=text,
        widget=forms.Select({'class':'form-select'}),
    )
    
class repiarForm(forms.Form):
    field1 = forms.BooleanField(
        required=False,
        label='เปิดคอมพิวเตอร์มาแล้วขึ้นหน้าจอฟ้า',
        initial=False,
        widget=forms.CheckboxInput(attrs={'id':'lb_repair01',})
    )
    field2 = forms.BooleanField(
        required=False,
        label='หน้าจอคอมพิวเตอร์เปิดไม่ติด',
        initial=False,
        widget=forms.CheckboxInput(attrs={'id':'lb_repair01'})
    )
    field3 = forms.BooleanField(
        required=False,
        label='คอมพิวเตอร์มีเสียงร้องตอนเปิดเครื่อง',
        initial=False,
        widget=forms.CheckboxInput(attrs={'id':'lb_repair01'})
    )

    # https://docs.djangoproject.com/en/3.1/topics/forms/
    # https://pypi.org/project/django-bootstrap-modal-forms/2.0.0/
    # https://stackoverflow.com/questions/37170465/how-to-get-value-checkbox-on-modal-bootstrap
    # boolean Field   https://www.youtube.com/watch?v=C4P5fiAC7QA&ab_channel=DJanGO