# Generated by Django 2.0.5 on 2019-03-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nitto', '0003_auto_20190303_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nitto',
            name='condition',
        ),
        migrations.AddField(
            model_name='nitto',
            name='band',
            field=models.CharField(default='compahy', max_length=20),
        ),
    ]
