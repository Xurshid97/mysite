# Generated by Django 5.0.5 on 2024-05-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkshare", "0012_remove_link_image_image_category_image_link_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="category",
        ),
        migrations.RemoveField(
            model_name="image",
            name="link",
        ),
        migrations.RemoveField(
            model_name="image",
            name="user",
        ),
        migrations.AddField(
            model_name="link",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="link_images/"),
        ),
    ]
