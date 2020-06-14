# Generated by Django 3.0.5 on 2020-06-14 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn_number', models.CharField(max_length=15)),
                ('book_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]