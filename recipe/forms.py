from .models import Post, Ingredient
from django import forms

# class recipeForm(forms.ModelForm):
#     class Meta:
#         model= Post

# class ingredientForm(forms.ModelForm):
#     class Meta:
#         model= Ingredient


class PostSearchForm(forms.Form):
   search_text= forms.CharField(
            required=False,
            widget=forms.TextInput(attrs={
                'placeholder:':'Search Your Favourite Recipe here',
                'class':'form-control mr-sm-2',
                'type':'search',
                'aria-label':'Search',
            }),
   )