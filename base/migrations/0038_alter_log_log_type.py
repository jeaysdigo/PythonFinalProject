# Generated by Django 5.0 on 2023-12-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_alter_choice_is_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log_type',
            field=models.CharField(choices=[('register', ' successfully registered their account.'), ('login', ' logged in their account.'), ('enroll', ' enrolled to a course.'), ('takeQuiz', ' take a quiz'), ('finishQuiz', ' finished a quiz'), ('viewLesson', ' viewed a lesson'), ('finishCourse', ' finished a course.'), ('obtainBadge', 'obtained a badge.'), ('obtainCert', 'obtained a certificate.'), ('default', ' default')], default='default', max_length=100),
        ),
    ]
