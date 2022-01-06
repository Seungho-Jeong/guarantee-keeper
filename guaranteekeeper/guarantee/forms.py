from django import forms

from .models import Guarantee


class GuaranteeForm(forms.ModelForm):
    class Meta:
        model = Guarantee
        fields = '__all__'
