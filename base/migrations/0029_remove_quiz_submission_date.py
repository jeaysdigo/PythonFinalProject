# Generated by Django 4.2.7 on 2023-12-10 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_quiz_submission_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='submission_date',
        ),
    ]
