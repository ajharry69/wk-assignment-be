# Generated by Django 3.0.7 on 2020-06-28 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('person',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='person.Person')),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('altitude', models.FloatField(default=0)),
                ('name', models.CharField(blank=True, default=None, max_length=150, null=True)),
            ],
        ),
    ]