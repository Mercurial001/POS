# Generated by Django 3.2.23 on 2023-12-15 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20231210_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]