from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['code', 'name', 'category', 'stock', 'location', 'status', 'price']
        labels = {
            'code': 'รหัสอุปกรณ์ / บาร์โค้ด',
            'name': 'ชื่ออุปกรณ์',
            'category': 'หมวดหมู่อุปกรณ์',
            'stock': 'จำนวนคงเหลือในคลัง',
            'location': 'สถานที่จัดเก็บ / โซน',
            'status': 'สถานะอุปกรณ์',
            'price': 'ราคาต่อหน่วย (บาท)',
        }
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'เช่น EQ-CARDIO-001'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'เช่น ลู่วิ่งไฟฟ้า Commercial Treadmill'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select bg-dark text-white border-secondary'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'min': '0',
                'placeholder': 'ระบุจำนวนชิ้น'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'เช่น โซน Cardio ชั้น 2'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select bg-dark text-white border-secondary'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'step': '0.01',
                'placeholder': '0.00'
            }),
        }