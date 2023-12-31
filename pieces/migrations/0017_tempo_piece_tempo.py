# Generated by Django 4.2.2 on 2023-11-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0016_period_sorting_order_typeofpiece_sorting_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sorting_order', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='piece',
            name='tempo',
            field=models.ManyToManyField(to='pieces.tempo'),
        ),
    ]
