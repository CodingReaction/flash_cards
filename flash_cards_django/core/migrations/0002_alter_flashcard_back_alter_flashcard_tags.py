# Generated by Django 4.2.3 on 2023-07-28 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='back',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.tag'),
        ),
    ]
