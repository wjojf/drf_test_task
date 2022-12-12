# Generated by Django 4.1.4 on 2022-12-12 13:13

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('number', models.PositiveIntegerField(unique=True)),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[(1, 'In stock'), (2, 'Preorder'), (3, 'Arrival expected'), (4, 'Not Avaliable'), (5, 'Not manufactured')], max_length=255)),
                ('image', models.ImageField(upload_to=core.utils.image_directory_path)),
            ],
        ),
    ]