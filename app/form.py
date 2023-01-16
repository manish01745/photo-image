from django import forms
from .models import uploder


class img(forms.ModelForm):
    class Meta:
        model = uploder
        fields = "__all__"
        labels = {'image':''}