# Generated by Django 4.2.5 on 2023-09-07 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement_app', '0002_remove_advertisement_advertisement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='advertisement_date',
            field=models.DateField(auto_now=True),
        ),
    ]