# Generated by Django 3.2 on 2022-01-20 09:52

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolog', '0008_auto_20220119_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='friends',
            field=models.ManyToManyField(blank=True, to='photolog.Account'),
        ),
        migrations.AddField(
            model_name='account',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
