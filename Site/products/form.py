from logging import PlaceHolder
# form systeme
from django import forms
from .models import Products
# authentif system
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    """model form for user"""
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]



class ProductForm(forms.ModelForm):
    """form facile"""
    error_css_class = 'error-field'
    required_css_class = 'required-field'
# ceci est copier de la clsas en dessou ca fais plus rapide
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Product name',
            "class": "form-control",
        }
    ))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter product description ',
            'rows':5,
            'cols':30,
            'class': 'form-label',
            'id': 'my_id',
        }
    ))
    price = forms.DecimalField(initial=0)
    image = forms.ImageField(label='Image', required=False)
    slug = forms.SlugField(label='',widget= forms.TextInput(
        attrs={'placeholder': 'Enter slug '}))
    
    
    
    
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'slug', 'activate' )
    
    
    def clean_price(self, *args, **kwargs):
        """verifie donnee condition"""
        price = self.cleaned_data.get('price')
        if not price >= 1 :
            raise forms.ValidationError('ca doit etre sup ou egal a 1')
        elif not  price <= 100:
            raise forms.ValidationError('ca doit etre inf ou egal a 100')
        else:
            return price
            
    
    
    
    
    
    
    
class RowProductForm(forms.Form):
    """form difficile (en view)"""
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={"class": "form-control",'placeholder': 'Product name',}
    ))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'placeholder': 'Enter product description ',
            'rows':5,
            'cols':30,
            'class': 'descr',
            'id': 'my_id',
        }
    ))
    price = forms.DecimalField(initial=0)
    image = forms.ImageField(label='Image', required=False)
    slug = forms.CharField(label='Slug',)
    