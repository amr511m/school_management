# Generated by Django 3.0 on 2020-08-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200822_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ['class_number']},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classrooms',
            field=models.ManyToManyField(related_name='classroom_teachers', to='school.Classroom'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='classroom',
            order_with_respect_to=None,
        ),
    ]
