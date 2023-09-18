# Generated by Django 4.2.2 on 2023-06-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='composer',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='composer',
            name='last_name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
