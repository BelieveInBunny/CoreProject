# Generated by Django 4.0.3 on 2022-03-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0039_remove_animeinfomodel_episodes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animeinfomodel",
            name="episodes",
            field=models.ManyToManyField(blank=True, to="upload.episodemodel"),
        ),
    ]
