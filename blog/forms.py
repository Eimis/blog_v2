from django import forms


class EmailForm(forms.Form):
    name = forms.CharField()
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
