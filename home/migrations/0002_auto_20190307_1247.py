# Generated by Django 2.0.5 on 2019-03-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customar_Parmanent_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customar_present_address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='example_address', max_length=300),
        ),
    ]