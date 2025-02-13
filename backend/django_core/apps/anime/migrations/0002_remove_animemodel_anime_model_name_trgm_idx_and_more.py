# Generated by Django 4.2a1 on 2023-02-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0001_initial"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="animemodel",
            name="anime_model_name_trgm_idx",
        ),
        migrations.RemoveIndex(
            model_name="animemodel",
            name="anime_name_japanese_trgm_idx",
        ),
        migrations.RemoveIndex(
            model_name="animenamesynonymmodel",
            name="anime_name_synonym_trgm_idx",
        ),
        migrations.AlterField(
            model_name="animemodel",
            name="name",
            field=models.CharField(db_index=True, max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name="animemodel",
            name="name_japanese",
            field=models.CharField(blank=True, db_index=True, default="", max_length=1024),
        ),
        migrations.AlterField(
            model_name="animenamesynonymmodel",
            name="name",
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
