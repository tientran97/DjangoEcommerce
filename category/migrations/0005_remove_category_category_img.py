# Generated by Django 4.2.6 on 2023-10-09 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_remove_category_category_ca_categor_7bd94b_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_img',
        ),
    ]
