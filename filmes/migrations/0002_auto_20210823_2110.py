# Generated by Django 3.1.7 on 2021-08-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='visto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='filme',
            name='avaliation',
            field=models.FloatField(),
        ),
    ]