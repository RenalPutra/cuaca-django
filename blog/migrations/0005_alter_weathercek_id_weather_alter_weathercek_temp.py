# Generated by Django 4.1.3 on 2022-12-21 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_weathercek_temp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weathercek",
            name="id_weather",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="weathercek",
            name="temp",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
