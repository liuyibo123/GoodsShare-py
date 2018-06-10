from __future__ import unicode_literals
from django import forms
from .models import Goods
class GoodsForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)
    class Meta:
        model=Goods
        fields=(
            'name','trade_type','price',
            'location','publisher','type','qq','phone','created_time',
        )