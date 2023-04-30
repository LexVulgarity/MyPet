from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','describe']
        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name of recipe',
            }),
            'describe': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe',
            })
        }