# Generated by Django 3.2.23 on 2023-11-23 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0004_alter_scannedproducts_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('sold_quantity', models.IntegerField()),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='soldproducts',
            name='cashier',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SoldProductHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('product', models.ManyToManyField(to='management.SoldProduct')),
            ],
        ),
        migrations.AlterField(
            model_name='soldproducts',
            name='product',
            field=models.ManyToManyField(to='management.SoldProduct'),
        ),
    ]