# Generated by Django 3.1.3 on 2020-11-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
