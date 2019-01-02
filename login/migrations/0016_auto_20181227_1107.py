# Generated by Django 2.1.4 on 2018-12-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_auto_20181227_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_number',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
