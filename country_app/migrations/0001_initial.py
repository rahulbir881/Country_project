# Generated by Django 3.0.6 on 2020-05-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flag', models.ImageField(upload_to='pics')),
                ('area', models.IntegerField()),
                ('population', models.IntegerField()),
                ('capital', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=50)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country_app.Continent')),
            ],
        ),
    ]
