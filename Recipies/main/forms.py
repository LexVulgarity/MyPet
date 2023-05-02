from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea,FileInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','describe','image']
        '''widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name of recipe',
            }),
            'describe': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe',
            }),
        }'''