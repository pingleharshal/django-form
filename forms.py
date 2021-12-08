from django import forms


class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    #available = forms.BooleanField()
    date = forms.DateField(widget=forms.SelectDateWidget)
