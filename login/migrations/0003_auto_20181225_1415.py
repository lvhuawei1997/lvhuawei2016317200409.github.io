# Generated by Django 2.1.4 on 2018-12-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_iden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='iden',
            field=models.CharField(choices=[('farmer', '农场主'), ('technician', '技术人员'), ('marketer', '市场人员')], default='农场主', max_length=32),
        ),
    ]
