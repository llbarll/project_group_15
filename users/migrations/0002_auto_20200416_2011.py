# Generated by Django 3.0.4 on 2020-04-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='citizen',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='secretary',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
