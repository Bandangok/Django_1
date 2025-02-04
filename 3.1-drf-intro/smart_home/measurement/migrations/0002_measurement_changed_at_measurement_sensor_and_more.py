# Generated by Django 5.0.6 on 2024-06-16 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="measurement",
            name="changed_at",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="measurement",
            name="sensor",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="measurement.sensor",
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="temperature",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
