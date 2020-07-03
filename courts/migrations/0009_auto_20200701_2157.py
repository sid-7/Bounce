# Generated by Django 3.0.7 on 2020-07-02 02:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0008_auto_20200620_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='court',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='court',
            name='county',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='court',
            name='id',
            field=models.CharField(default=uuid.UUID('92722a8c-05bd-4fb3-a40d-b0c13d3837e8'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
