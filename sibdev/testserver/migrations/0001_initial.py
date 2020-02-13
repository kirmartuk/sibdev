# Generated by Django 2.2.10 on 2020-02-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.TextField()),
                ('item', models.TextField()),
                ('total', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]