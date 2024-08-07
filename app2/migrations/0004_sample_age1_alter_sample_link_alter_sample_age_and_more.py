# Generated by Django 5.0.4 on 2024-04-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_sample_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='age1',
            field=models.IntegerField(default='hello', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Link',
            field=models.URLField(default='hello'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='age',
            field=models.IntegerField(default='hello'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='email_id',
            field=models.EmailField(default='hello', max_length=254),
        ),
        migrations.AlterField(
            model_name='sample',
            name='gender',
            field=models.CharField(default='hello', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(default='hello', max_length=50),
        ),
        migrations.AlterField(
            model_name='sample',
            name='phone_no',
            field=models.IntegerField(default='hello', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='resume',
            field=models.FileField(default='hello', upload_to=''),
        ),
    ]
