# Generated by Django 4.2.7 on 2023-11-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("metadata", models.JSONField(default=dict)),
                ("name", models.CharField(max_length=255)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
