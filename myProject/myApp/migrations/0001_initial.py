# Generated by Django 4.2.8 on 2023-12-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student_Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Department", models.CharField(max_length=100)),
                ("City", models.CharField(max_length=100)),
            ],
        ),
    ]
