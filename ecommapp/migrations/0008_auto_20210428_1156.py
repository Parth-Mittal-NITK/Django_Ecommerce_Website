# Generated by Django 3.1.7 on 2021-04-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0007_auto_20210428_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]