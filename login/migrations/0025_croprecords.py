# Generated by Django 2.1.4 on 2018-12-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_auto_20181229_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('croprecords_date', models.CharField(max_length=15)),
                ('land_id', models.CharField(max_length=10)),
                ('tlc', models.CharField(max_length=10, null=True)),
                ('crop_name', models.CharField(max_length=10)),
                ('naworm', models.CharField(default='无', max_length=32)),
                ('nanosu', models.CharField(default='无', max_length=32)),
            ],
        ),
    ]
