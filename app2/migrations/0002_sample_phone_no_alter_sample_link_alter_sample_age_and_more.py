# Generated by Django 5.0.4 on 2024-04-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='email_id',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
