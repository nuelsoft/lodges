# Generated by Django 2.0.5 on 2018-07-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodges', '0004_lodge_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]