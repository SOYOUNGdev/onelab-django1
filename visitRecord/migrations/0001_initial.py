# Generated by Django 5.0.2 on 2024-03-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_visit_record',
            },
        ),
    ]