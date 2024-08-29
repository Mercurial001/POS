# Generated by Django 3.2.23 on 2023-11-22 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_auto_20231121_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashierDynamicProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('scanned_quantity', models.IntegerField(default=1)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]