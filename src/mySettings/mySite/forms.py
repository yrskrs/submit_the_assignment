from django import forms
from .models import *

class UploadForm(forms.Form):
    #files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    text_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'full-width'}),max_length=255)
    file_field = forms.FileField(required=False)
    link_field = forms.URLField(widget=forms.TextInput(attrs={'class': 'full-width'}),required=False)

    def get_choices():
    # Логіка для отримання варіантів з бази даних або інших джерел
        return [
            ('5А', '5А'), 
            ('5Б', '5Б'),
            ('5В', '5В'), 
            ('5Г', '5Г'),
            ('6А', '6А'), 
            ('6Б', '6Б'),
            ('6В', '6В'), 
            ('7А', '7А'),
            ('7Б', '7Б'), 
            ('7В', '7В'),
            
            
            
            
            
            ]


    my_choice = forms.ChoiceField(choices=get_choices)
