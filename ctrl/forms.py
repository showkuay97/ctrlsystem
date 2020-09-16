from django import forms
class create_repair(forms.Form):
    id_lb =forms.CharField(max_length=255)
    subject = forms.CheckboxInput()



    # https://docs.djangoproject.com/en/3.1/topics/forms/
    # https://pypi.org/project/django-bootstrap-modal-forms/2.0.0/
    # https://stackoverflow.com/questions/37170465/how-to-get-value-checkbox-on-modal-bootstrap