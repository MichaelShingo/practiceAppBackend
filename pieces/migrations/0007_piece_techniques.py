# Generated by Django 4.2.2 on 2023-06-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0006_remove_piece_techniques'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='techniques',
            field=models.ManyToManyField(to='pieces.technique'),
        ),
    ]
