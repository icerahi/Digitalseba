# Generated by Django 2.0.5 on 2019-03-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0002_gift_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gift',
            name='condition',
            field=models.CharField(default='New', max_length=20),
        ),
    ]
