from django import forms
from .models import ip


class ipForm(forms.ModelForm):
    class Meta:
        model = ip
        fields = "__all__"
