# Generated by Django 4.2.6 on 2023-10-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_remove_category_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(blank=True, upload_to='photos/categories'),
        ),
    ]
