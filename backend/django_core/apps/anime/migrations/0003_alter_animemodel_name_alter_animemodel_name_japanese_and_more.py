# Generated by Django 4.2a1 on 2023-02-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0002_remove_animemodel_anime_model_name_trgm_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animemodel",
            name="name",
            field=models.CharField(max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name="animemodel",
            name="name_japanese",
            field=models.CharField(blank=True, default="", max_length=1024),
        ),
        migrations.AlterField(
            model_name="animenamesynonymmodel",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
