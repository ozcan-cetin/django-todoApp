from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
        'myfield': forms.TextInput(attrs={'class': 'form-control'}),
      }