# Generated by Django 4.2.5 on 2023-09-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
