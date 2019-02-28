from django import forms

class userinput(forms.Form):
    input_sentence=forms.CharField(max_length=500)