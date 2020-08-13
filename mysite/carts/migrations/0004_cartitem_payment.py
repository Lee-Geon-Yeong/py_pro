# Generated by Django 3.1 on 2020-08-13 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20200813_0733'),
        ('carts', '0003_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='payment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='payments.payment'),
        ),
    ]