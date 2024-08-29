# Generated by Django 3.2.23 on 2024-03-22 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0024_usercreationvalidation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name_plural': 'Income'},
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to='auth.user'),
            preserve_default=False,
        ),
    ]