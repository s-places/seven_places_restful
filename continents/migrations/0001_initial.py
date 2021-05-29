# Generated by Django 3.0.5 on 2021-03-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20)),
                ('place', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('polulation', models.PositiveIntegerField(blank=True)),
                ('history', models.TextField(blank=True)),
                ('languages', models.CharField(blank=True, max_length=40)),
                ('first_image', models.ImageField(blank=True, upload_to='')),
                ('second_image', models.ImageField(blank=True, upload_to='')),
                ('third_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]