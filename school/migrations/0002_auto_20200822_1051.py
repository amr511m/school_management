# Generated by Django 3.0 on 2020-08-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='national_id',
            field=models.IntegerField(),
        ),
    ]
