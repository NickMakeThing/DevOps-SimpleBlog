# Generated by Django 4.0.2 on 2022-02-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_alter_images_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
