# Generated by Django 5.1.3 on 2024-12-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Place', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
