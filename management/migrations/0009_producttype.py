# Generated by Django 3.2.23 on 2023-12-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_soldoutproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=255)),
            ],
        ),
    ]