# Generated by Django 4.2.7 on 2023-12-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_yourmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='units',
            field=models.ManyToManyField(related_name='lessons', to='base.unit'),
        ),
    ]
