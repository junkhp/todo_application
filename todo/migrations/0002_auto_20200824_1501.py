# Generated by Django 2.2.15 on 2020-08-24 06:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('warning', 'high'), ('secondary', 'normal'), ('light', 'low')], default='warning', max_length=50),
            preserve_default=False,
        ),
    ]
