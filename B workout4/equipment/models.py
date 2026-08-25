from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'พร้อมใช้งาน'),
        ('maintenance', 'ส่งซ่อม/บำรุง'),
        ('out_of_stock', 'สินค้าหมดสต็อก'),
    ]

    CATEGORY_CHOICES = [
        ('cardio', 'เครื่องคาร์ดิโอ (Cardio)'),
        ('strength', 'เครื่องเวทเทรนนิ่ง (Strength)'),
        ('freeweight', 'ฟรีเวทและดัมเบล (Free Weights)'),
        ('accessories', 'อุปกรณ์เสริม/เซฟตี้ (Accessories)'),
    ]

    code = models.CharField(max_length=50, unique=True, verbose_name="รหัสอุปกรณ์/บาร์โค้ด")
    name = models.CharField(max_length=150, verbose_name="ชื่ออุปกรณ์")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="หมวดหมู่อุปกรณ์")
    stock = models.IntegerField(default=1, verbose_name="จำนวนคงเหลือในคลัง")
    location = models.CharField(max_length=100, default="โซนหลัก", verbose_name="สถานที่จัดเก็บ/โซน")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="สถานะ")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="ราคาต่อหน่วย (บาท)")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="อัปเดตล่าสุด")

    def __str__(self):
        return f"{self.code} - {self.name}"