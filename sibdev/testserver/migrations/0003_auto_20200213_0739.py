# Generated by Django 2.2.10 on 2020-02-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testserver', '0002_auto_20200213_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='date',
            field=models.DateTimeField(),
        ),
    ]