# Generated by Django 2.0.5 on 2019-03-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panjabi', '0002_panjabi_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='panjabi',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='panjabi',
            name='condition',
            field=models.CharField(default='New', max_length=20),
        ),
    ]