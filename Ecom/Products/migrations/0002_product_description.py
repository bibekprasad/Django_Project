# Generated by Django 2.2.7 on 2019-11-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
