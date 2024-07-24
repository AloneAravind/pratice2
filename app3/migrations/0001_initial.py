# Generated by Django 5.0.4 on 2024-04-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('reg_num', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]