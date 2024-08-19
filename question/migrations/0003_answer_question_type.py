# Generated by Django 4.2.11 on 2024-08-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_alter_question_section_alter_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_type',
            field=models.CharField(choices=[('radio', 'Radio'), ('input', 'Input'), ('textarea', 'Textarea')], max_length=10, null=True),
        ),
    ]
