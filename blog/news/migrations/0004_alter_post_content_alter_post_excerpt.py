# Generated by Django 4.2.2 on 2023-06-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(verbose_name='Bajada'),
        ),
    ]