# Generated by Django 4.0.3 on 2022-03-16 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0013_remove_episodemodel_episode_comment_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="episodemodel",
            old_name="episode_number",
            new_name="id",
        ),
    ]
