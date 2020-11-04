# Generated by Django 3.1.3 on 2020-11-04 16:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(max_length=300)),
                ('describtion', ckeditor.fields.RichTextField(max_length=260)),
                ('timer', models.CharField(max_length=150)),
                ('button_text', models.CharField(max_length=36, null=True)),
                ('modal_title', models.CharField(max_length=150, null=True)),
                ('modal_describtion', ckeditor.fields.RichTextField(max_length=150, null=True)),
                ('facebook', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('telegram', models.CharField(max_length=150)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
            ],
        ),
    ]
