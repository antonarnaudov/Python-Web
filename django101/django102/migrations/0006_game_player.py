# Generated by Django 3.1.1 on 2020-10-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0005_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ManyToManyField(to='django102.Player'),
        ),
    ]
