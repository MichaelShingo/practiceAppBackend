# Generated by Django 4.2.2 on 2023-06-26 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tutorial', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('difficulty', models.IntegerField()),
                ('recording_link', models.URLField(blank=True, null=True)),
                ('tutorial_link', models.URLField(blank=True, null=True)),
                ('composer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pieces.composer')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pieces.period')),
                ('prereqs', models.ManyToManyField(to='pieces.piece')),
                ('techniques', models.ManyToManyField(to='pieces.technique')),
                ('type_of_piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pieces.typeofpiece')),
            ],
        ),
    ]
