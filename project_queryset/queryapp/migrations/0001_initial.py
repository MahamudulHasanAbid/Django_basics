# Generated by Django 5.0.4 on 2024-04-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
                ('pass_date', models.DateField()),
            ],
        ),
    ]