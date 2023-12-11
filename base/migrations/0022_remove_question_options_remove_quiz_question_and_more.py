# Generated by Django 4.2.7 on 2023-12-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_question_lesson_remove_question_quiz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='quizzes', to='base.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1),
        ),
    ]
