# Generated by Django 4.2.5 on 2023-09-07 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carmodel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_owners', models.IntegerField()),
                ('registration_number', models.IntegerField()),
                ('manufacture_year', models.IntegerField()),
                ('number_of_doors', models.IntegerField()),
                ('milege', models.IntegerField()),
                ('car_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carmodel_app.carmodel')),
            ],
        ),
    ]