# Generated by Django 2.0.5 on 2019-03-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pant', '0003_auto_20190303_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pant',
            name='condition',
        ),
        migrations.AddField(
            model_name='pant',
            name='band',
            field=models.CharField(default='d comanpy', max_length=20),
        ),
    ]
