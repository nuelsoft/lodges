# Generated by Django 2.0.5 on 2018-07-18 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='sex',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
