# Generated by Django 4.2.2 on 2023-06-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
