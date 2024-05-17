# Generated by Django 5.0.5 on 2024-05-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkshare', '0005_category_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='savedcategories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]