from django import forms
from django.core.exceptions import ValidationError


class coreForm(forms.Form):

    name = forms.CharField(max_length=50)
    email = forms.EmailField()



# def checkName(value):
#
#     if value.isdigit():
#         raise ValidationError("dgdrt")
#
# def checkEmail(value):
#
#     if value.find('mytectra.com') == -1:
#
#         raise ValidationError("please provide mytectra.com email!")

class formExample(forms.Form):

    ch = (

        ('', '--Select options--'),
        ('pn', 'Pune'),
        ('bng', 'Bangalore'),
        ('hyd', 'Hyderabad')
    )
    gn = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    name = forms.CharField(label="UserName",min_length=5, max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    city = forms.ChoiceField(choices=ch)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    active = forms.CharField(widget=forms.CheckboxInput())

    def clean(self):

        form_data = self.cleaned_data

        if 'email' in form_data and form_data['email'].find('mytectra.com') == -1:
            self.errors['email'] = ['please provide mytectra.com email!']

        if 'name' in form_data and form_data['name'].isdigit():
            self.errors['name'] = ['name must be in characters!']


        return form_data

