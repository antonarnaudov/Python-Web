# Generated by Django 3.1.1 on 2020-10-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0008_auto_20201011_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='level_of_difficulty',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=2),
        ),
    ]