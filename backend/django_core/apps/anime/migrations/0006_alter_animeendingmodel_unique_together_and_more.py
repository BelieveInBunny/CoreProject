# Generated by Django 4.1.7 on 2023-03-22 15:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0005_alter_animeendingmodel_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="animeendingmodel",
            unique_together={("entry", "name", "url")},
        ),
        migrations.AlterUniqueTogether(
            name="animeopeningmodel",
            unique_together={("entry", "name", "url")},
        ),
    ]
