from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )


class TodoForm(forms.Form):
    title = forms.CharField(label='Todo Title', required=True)
    description = forms.CharField(label='Todo Description', required=True)
    # is_active = forms.BooleanField(required=False)
