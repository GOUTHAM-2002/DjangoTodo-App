from django import forms
from .models import Categories,Todos

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title','category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your task'}),
            'category':forms.Select()
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

