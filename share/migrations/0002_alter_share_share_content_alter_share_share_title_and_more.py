# Generated by Django 5.0.2 on 2024-05-23 09:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("share", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="share",
            name="share_content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="share",
            name="share_title",
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name="ShareFileContent",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("text", models.TextField()),
                ("file_name", models.CharField(max_length=255)),
                (
                    "share",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="share.share"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_share_file_content",
            },
        ),
    ]
