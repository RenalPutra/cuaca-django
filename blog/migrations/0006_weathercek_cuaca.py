# Generated by Django 4.1.3 on 2022-12-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_weathercek_id_weather_alter_weathercek_temp"),
    ]

    operations = [
        migrations.AddField(
            model_name="weathercek",
            name="cuaca",
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]