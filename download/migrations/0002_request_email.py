# Generated by Django 2.2.1 on 2019-06-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='email',
            field=models.EmailField(default=False, max_length=100),
        ),
    ]