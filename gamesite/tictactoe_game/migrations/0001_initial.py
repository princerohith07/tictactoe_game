# Generated by Django 5.0.2 on 2024-02-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("board", models.CharField(default="---------", max_length=9)),
                ("next_to_move", models.CharField(default="X", max_length=1)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("P", "Playing"),
                            ("X", "X Wins"),
                            ("O", "O Wins"),
                            ("D", "Draw"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]
