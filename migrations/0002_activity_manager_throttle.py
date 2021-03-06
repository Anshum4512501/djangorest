# Generated by Django 3.0.5 on 2020-04-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('end_time_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(max_length=50)),
                ('activity', models.ManyToManyField(to='program.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Throttle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ok', models.BooleanField(default=True)),
                ('manager', models.ManyToManyField(to='program.Manager')),
            ],
        ),
    ]
