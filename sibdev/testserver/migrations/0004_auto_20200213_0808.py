# Generated by Django 2.2.10 on 2020-02-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testserver', '0003_auto_20200213_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='date',
            field=models.DateField(),
        ),
    ]
