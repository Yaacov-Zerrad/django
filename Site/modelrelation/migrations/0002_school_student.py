# Generated by Django 4.0 on 2022-06-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('school', models.ManyToManyField(to='modelrelation.School')),
            ],
        ),
    ]
