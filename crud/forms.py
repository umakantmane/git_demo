from django import forms

from crud.models import Bank,Customer

class bankForm(forms.ModelForm):

    #name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    #email = forms.EmailField(disabled=True)
    class Meta:
        model = Bank
        fields = ('name','email', 'address')


class customerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'bank', 'email')