# Generated by Django 3.1 on 2020-08-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0011_auto_20200817_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]