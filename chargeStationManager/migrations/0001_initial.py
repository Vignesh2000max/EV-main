# Generated by Django 3.2 on 2021-06-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChargePoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('point_number', models.CharField(max_length=50)),
                ('occupied', models.BooleanField(default=False)),
            ],
        ),
    ]
