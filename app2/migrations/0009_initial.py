# Generated by Django 5.0.4 on 2024-04-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app2', '0008_delete_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='hello', max_length=50)),
                ('age', models.IntegerField(default=1)),
                ('resume', models.FileField(default='hello', upload_to='')),
                ('email_id', models.EmailField(default='hello', max_length=254)),
                ('Link', models.URLField(default='hello')),
                ('phone_no', models.IntegerField(default=1, null=True)),
                ('gender', models.CharField(default='hello', max_length=20, null=True)),
            ],
        ),
    ]
