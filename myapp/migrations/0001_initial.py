# Generated by Django 2.2.27 on 2022-03-05 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=20)),
                ('phone', models.CharField(max_length=16)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
