# Generated by Django 3.2.23 on 2023-12-10 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_producttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashierdynamicproducts',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='management.producttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='management.producttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldoutproduct',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='management.producttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldproduct',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='management.producttype'),
            preserve_default=False,
        ),
    ]
