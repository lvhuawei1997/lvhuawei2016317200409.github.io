# Generated by Django 2.1.4 on 2018-12-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='remark',
            field=models.CharField(default='无', max_length=32),
        ),
    ]
