# Generated by Django 3.0.6 on 2020-05-31 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200531_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='board',
            new_name='boards',
        ),
    ]
