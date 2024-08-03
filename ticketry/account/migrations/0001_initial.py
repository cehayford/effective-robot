# Generated by Django 5.0.7 on 2024-08-03 07:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UserId')),
                ('first_name', models.TextField(blank=True, max_length=25)),
                ('last_name', models.TextField(blank=True, max_length=25)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('user_address', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]
