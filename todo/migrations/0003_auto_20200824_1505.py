# Generated by Django 2.2.15 on 2020-08-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200824_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('secondary', 'normal'), ('light', 'low')], max_length=50),
        ),
    ]