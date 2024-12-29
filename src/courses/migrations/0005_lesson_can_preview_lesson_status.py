# Generated by Django 5.1.4 on 2024-12-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='can_preview',
            field=models.BooleanField(default=False, help_text='If the user does not have access to the course, they can preview this lesson.'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('pub', 'Published'), ('soon', 'Coming Soon'), ('draft', 'Draft')], default='pub', max_length=10),
        ),
    ]
