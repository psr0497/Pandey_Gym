# Generated by Django 3.0.3 on 2020-03-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20200324_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='img_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
