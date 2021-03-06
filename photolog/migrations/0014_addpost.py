# Generated by Django 3.2 on 2022-04-19 11:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolog', '0013_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('featured_image', models.ImageField(upload_to='images/')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
