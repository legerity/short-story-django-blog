# Generated by Django 3.1 on 2020-09-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_remove_story_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
