# Generated by Django 3.2.23 on 2023-12-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20231215_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashierdynamicproducts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]