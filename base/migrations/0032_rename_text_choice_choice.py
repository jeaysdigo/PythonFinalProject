# Generated by Django 4.2.7 on 2023-12-10 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_quiz_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='text',
            new_name='choice',
        ),
    ]
