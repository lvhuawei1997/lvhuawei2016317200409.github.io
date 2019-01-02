from django.db import models

# Create your models here.


class User(models.Model):

    identity = (
        ('farmer', "农场主"),
        ('technician', "技术人员"),
        ('marketer', "市场人员"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    identity = models.CharField(max_length=32, choices=identity, default="农场主")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Land(models.Model):

    zone = models.CharField(max_length=32)
    landmark = models.CharField(max_length=32)
    lot = models.CharField(max_length=32, null=True)
    position = models.CharField(max_length=32)
    area = models.CharField(max_length=128)

    def __str__(self):
        return self.id


class Product(models.Model):

    purchase_date = models.CharField(max_length=15)
    product_name = models.CharField(max_length=10)
    purchase_number = models.CharField(max_length=10)
    purchase_price = models.CharField(max_length=10)
    remark = models.CharField(max_length=32, default="无")

    def __str__(self):
        return self.id


class Dosage(models.Model):

    dosage_date = models.CharField(max_length=15)
    muck_name = models.CharField(max_length=10)
    tlc = models.CharField(max_length=10, null=True)
    twlr = models.CharField(max_length=10)
    naworm = models.CharField(max_length=32, default="无")

    def __str__(self):
        return self.id


class CropRecords(models.Model):

    croprecords_date = models.CharField(max_length=15)
    land_id = models.CharField(max_length=10)
    tlc = models.CharField(max_length=10, null=True)
    crop_name = models.CharField(max_length=10)
    naworm = models.CharField(max_length=32, default="无")
    nanosu = models.CharField(max_length=32, default="无")

    def __str__(self):
        return self.id


class Recovery(models.Model):

    recovery_date = models.CharField(max_length=15)
    vegetables_name = models.CharField(max_length=10)
    recovery_number = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.id


