from django import forms
from .models import TeaItem

class TeaItemForm(forms.ModelForm):
    class Meta:
        model = TeaItem
        fields = ['name', 'price', 'stock', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น ชานมไต้หวันไข่มุก'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'จำนวนสต็อก'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'รายละเอียดเพิ่มเติม...'}),
        }