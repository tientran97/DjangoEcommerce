# Generated by Django 4.2.6 on 2023-10-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='nutrition',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
