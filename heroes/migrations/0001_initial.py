# Generated by Django 5.1.7 on 2025-05-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avenger',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
            ],
        ),
    ]
