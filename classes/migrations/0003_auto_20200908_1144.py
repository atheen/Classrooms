# Generated by Django 2.2.13 on 2020-09-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20200908_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_grade',
            field=models.FloatField(blank=True),
        ),
    ]
