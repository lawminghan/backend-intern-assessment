# Generated by Django 4.1.7 on 2023-03-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wavescanuser',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wavescanuser',
            name='designation',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
