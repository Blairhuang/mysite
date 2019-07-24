from django import forms


class numberForm(forms.Form):
    title = forms.CharField()
    r = forms.IntegerField(label='r')
    gens = forms.IntegerField(label='gens')
    a = forms.IntegerField(label='a')
    d = forms.IntegerField(label='d')
    c = forms.IntegerField(label='c')
    b = forms.IntegerField(label='b')
