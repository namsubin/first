# Generated by Django 4.0.7 on 2022-09-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]