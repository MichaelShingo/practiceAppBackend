# Generated by Django 4.2.2 on 2023-06-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0003_alter_piece_prereqs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='piece',
            name='prereqs',
            field=models.ManyToManyField(to='pieces.piece'),
        ),
    ]
