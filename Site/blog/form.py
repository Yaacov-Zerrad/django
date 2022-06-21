from django import forms
from .models import Articles


class modelForm(forms.ModelForm):
    """form facile"""
# ceci est copier de la clsas en dessou ca fais plus rapide
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            'placeholder': 'title',
            'class':'form-label',
        }
    ))
    content = forms.CharField(label='content', widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter content ',
            'rows':5,
            'cols':30,
            'class': 'form-label',
            'id': 'my_id',
        }
    ))
    
    
    class Meta:
        model = Articles
        fields = '__all__'
    