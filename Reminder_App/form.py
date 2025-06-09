from django import forms

class Form(forms.Form):
    date_time = forms.DateTimeField(label="Date - Time", widget=forms.DateTimeInput(attrs={"class" : "form-control", "type" : "datetime-local"}))
    location = forms.CharField(label="Location", widget=forms.TextInput(attrs={"class" : "form-control"}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"class" : "form-control", 'rows' : 2}))