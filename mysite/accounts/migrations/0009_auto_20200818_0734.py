# Generated by Django 3.1 on 2020-08-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200818_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='age',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.BooleanField(choices=[(0, 'Female'), (1, 'Male')], default=None, null=True, verbose_name='sex'),
        ),
    ]
