# Generated by Django 4.2.7 on 2023-12-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_rename_text_question_question_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='quiz',
            name='question',
            field=models.ManyToManyField(blank=True, related_name='questions', to='base.question'),
        ),
    ]