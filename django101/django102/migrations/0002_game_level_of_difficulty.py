# Generated by Django 3.1.1 on 2020-09-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
