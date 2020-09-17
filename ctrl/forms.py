from django import forms
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
        label='ห้องปฏิบัติการ  ',
        label_suffix='   ',
        choices=text,
    )
class repiarForm(forms.Form):
    text=[
        ('เปิดคอมพิวเตอร์มาแล้วขึ้นหน้าจอฟ้า','เปิดคอมพิวเตอร์มาแล้วขึ้นหน้าจอฟ้า'),
        ('คอมพิวเตอร์มีเสียงร้องตอนเปิดเครื่อง','คอมพิวเตอร์มีเสียงร้องตอนเปิดเครื่อง'),
        ('หน้าจอคอมพิวเตอร์เปิดไม่ติด','หน้าจอคอมพิวเตอร์เปิดไม่ติด'),
        ('เครื่องคอมพิวเตอร์ไม่มีโปรแกรม','เครื่องคอมพิวเตอร์ไม่มีโปรแกรม'),
        ('เครื่องคอมพิวเตอร์เปิดขึ้นมาแล้วไม่เข้าวินโดว์','เครื่องคอมพิวเตอร์เปิดขึ้นมาแล้วไม่เข้าวินโดว์'),
        ('เครื่องคอมพิวเตอร์โปรแกรมใช้งานไม่ได้','เครื่องคอมพิวเตอร์โปรแกรมใช้งานไม่ได้'),
    ]
    field = forms.BooleanField(
        
        check_test=text,
    )


    # https://docs.djangoproject.com/en/3.1/topics/forms/
    # https://pypi.org/project/django-bootstrap-modal-forms/2.0.0/
    # https://stackoverflow.com/questions/37170465/how-to-get-value-checkbox-on-modal-bootstrap
    # boolean Field   https://www.youtube.com/watch?v=C4P5fiAC7QA&ab_channel=DJanGO