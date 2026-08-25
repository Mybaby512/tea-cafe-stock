from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="ชื่อจริง")
    last_name = models.CharField(max_length=50, verbose_name="นามสกุล")
    email = models.EmailField(unique=True, verbose_name="อีเมล")
    phone = models.CharField(max_length=20, verbose_name="เบอร์โทรศัพท์")
    department = models.CharField(
        max_length=50,
        choices=[
            ('HR', 'ทรัพยากรบุคคล'),
            ('IT', 'เทคโนโลยีสารสนเทศ'),
            ('Sales', 'ฝ่ายขาย'),
            ('Marketing', 'การตลาด'),
        ],
        verbose_name="แผนก"
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="เงินเดือน")
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True, verbose_name="รูปโปรไฟล์")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"