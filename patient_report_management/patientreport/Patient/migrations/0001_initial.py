# Generated by Django 3.0.2 on 2020-01-25 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientfirstname', models.CharField(max_length=50)),
                ('patientlastname', models.CharField(max_length=50)),
                ('patientaddress', models.CharField(max_length=50)),
                ('patientemail', models.EmailField(max_length=25)),
                ('patientpassword', models.CharField(max_length=10)),
                ('patientnumber', models.IntegerField()),
                ('citizennumber', models.IntegerField()),
                ('login_date', models.DateField(default=datetime.date.today)),
                ('patientdob', models.DateField()),
                ('patientprofile', models.ImageField(upload_to='patientimage')),
                ('patientpin', models.CharField(default='abs', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='patientactivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('postid', models.IntegerField()),
                ('useractivity', models.CharField(default='blank', max_length=1000)),
                ('meme', models.ImageField(default='blank', upload_to='meme')),
                ('uploaddate', models.DateField(default=datetime.date.today)),
                ('patientprofile', models.ImageField(upload_to='patientimage')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Citizennumber', models.IntegerField()),
                ('Subject', models.CharField(max_length=100)),
                ('Patientfile', models.FileField(upload_to='Report')),
                ('Description', models.CharField(max_length=200)),
                ('Hospitalname', models.CharField(default='blank', max_length=50)),
                ('uploaddate', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
