from django import forms
from .models import Item

Input_Classes='w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields =('category','name','description','price','image',)
        widgets={
            'category':forms.Select(attrs={
                                    'class':Input_Classes}),
            'name':forms.TextInput(attrs={
                                    'class':Input_Classes}),
            'description':forms.Textarea(attrs={
                                    'class':Input_Classes}),
            'price':forms.TextInput(attrs={
                                    'class':Input_Classes}),
            'image':forms.FileInput(attrs={
                                    'class':Input_Classes}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model= Item
        fields =('name','description','price','image','is_sold')
        widgets={
           
            'name':forms.TextInput(attrs={
                                    'class':Input_Classes}),
            'description':forms.Textarea(attrs={
                                    'class':Input_Classes}),
            'price':forms.TextInput(attrs={
                                    'class':Input_Classes}),
            'image':forms.FileInput(attrs={
                                    'class':Input_Classes}),
        }
