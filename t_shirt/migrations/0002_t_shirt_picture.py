# Generated by Django 2.0.5 on 2019-03-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_shirt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_shirt',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='T-shirt'),
        ),
    ]
