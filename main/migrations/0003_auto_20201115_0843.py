# Generated by Django 3.1.3 on 2020-11-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_notes_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note_title',
            field=models.CharField(max_length=50),
        ),
    ]
