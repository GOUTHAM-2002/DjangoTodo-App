from django import forms
from .models import Todos,Categories

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['category', 'title']  # Reordered fields
        widgets = {

            'title': forms.TextInput(attrs={'placeholder': 'Enter your task', 'style': 'margin-bottom:20px;width: 50%; border: 1px solid #ccc; padding: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'}),
            'category': forms.Select(attrs={ 'style': 'margin-bottom:20px;width: 50%; border: 1px solid #ccc; padding: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);',})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['title','color']
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : 'New category..'}),
            'color' : forms.TextInput(attrs={'type':'color','placeholder' : 'Choose a color'})
        }

class TodoCompletedForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields=['completed']

