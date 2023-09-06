# Generated by Django 4.2.5 on 2023-09-06 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
