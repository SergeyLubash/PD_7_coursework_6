# Generated by Django 3.2.6 on 2022-12-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
