# Generated by Django 3.2 on 2021-04-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveIntegerField()),
            ],
        ),
    ]
