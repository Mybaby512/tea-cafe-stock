from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="ประเภทชา")

    def __str__(self):
        return self.name

class TeaItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ประเภท")
    name = models.CharField(max_length=150, verbose_name="ชื่อเมนูชา")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="ราคา (บาท)")
    stock = models.IntegerField(default=0, verbose_name="สต็อกคงเหลือ (แก้ว)")
    description = models.TextField(blank=True, null=True, verbose_name="รายละเอียด")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="อัปเดตล่าสุด")

    def __str__(self):
        return f"{self.name} ({self.stock} แก้ว)"