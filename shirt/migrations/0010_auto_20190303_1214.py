# Generated by Django 2.0.5 on 2019-03-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0009_shirt_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shirt',
            name='condition',
            field=models.CharField(default='New', max_length=20),
        ),
    ]
