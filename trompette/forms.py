from .models import Account
from django.forms import ModelForm, TextInput, Textarea,TimeInput

class CrtAcc(ModelForm):
    class Meta:
        model = Account
        fields = ['username']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Заголовок квака",
            }),
            'text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Квакнуть",
            }),
        }