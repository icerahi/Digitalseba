# Generated by Django 2.0.5 on 2019-02-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0005_auto_20190216_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
