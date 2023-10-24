from django import forms
from .models import Category

class createCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']
        widgets = {
            'categoryName' : forms.TextInput(attrs={'class' : "form-control form-control-user" , 'placeholder' : 'Masukan Nama Kategori'})
        }
        label = False
        max_length = 255