# Generated by Django 5.1.4 on 2024-12-14 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='access',
            field=models.CharField(choices=[('any', 'Anyone'), ('email', 'Email Required')], default='email', max_length=5),
        ),
    ]
