from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='اسم التصنيف'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='مفعل'
    )

    class Meta:
        verbose_name = 'تصنيف'
        verbose_name_plural = 'التصنيفات'

    def __str__(self):
        return self.name


class AgeRange(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='الفئة العمرية'
    )  # مثال: 3-5 سنوات

    class Meta:
        verbose_name = 'فئة عمرية'
        verbose_name_plural = 'الفئات العمرية'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='اسم اللعبة'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name='التصنيف'
    )
    age_range = models.ForeignKey(
        AgeRange,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='الفئة العمرية'
    )
    description = models.TextField(
        blank=True,
        verbose_name='الوصف'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='السعر'
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='الكمية المتوفرة'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='متاح للبيع'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإضافة'
    )

    class Meta:
        verbose_name = 'لعبة'
        verbose_name_plural = 'الألعاب'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='اللعبة'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='الصورة'
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='صورة رئيسية'
    )

    class Meta:
        verbose_name = 'صورة لعبة'
        verbose_name_plural = 'صور الألعاب'

    def __str__(self):
        return self.product.name
