# Generated by Django 4.2.7 on 2023-12-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_question_options_remove_quiz_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(blank=True, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], max_length=1, null=True),
        ),
    ]
