# Generated by Django 3.0 on 2020-08-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200822_1116'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='classroom',
            order_with_respect_to='level',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='classroom_teachers',
        ),
    ]
